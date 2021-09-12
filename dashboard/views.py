from django.shortcuts import render, redirect
from django.http import JsonResponse, QueryDict
from kubernetes import client, config
import os, hashlib, random
from k8s import k8s


# Create your views here.
@k8s.self_login_required
def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        token = request.POST.get('token', None)
        if token:
            if k8s.auth_check('token', token):
                request.session['is_login'] = True
                request.session['auth_type'] = 'token'
                request.session['token'] = token
                code = 0
                msg = '认证成功'
            else:
                print(e)
                code = 1
                msg = 'token无效'
        else:
            file_obj = request.FILES.get('file')
            random_str = hashlib.md5(str(random.random()).encode()).hexdigest()
            file_path = os.path.join('kubeconfig', random_str)
            try:
                with open(file_path, 'w', encoding='utf8') as f:
                    data = file_obj.read().decode()  # byte转str
                    f.write(data)
            except Exception:
                code = 1
                msg = '文件类型错误！'
            if k8s.auth_check('kubeconfig', random_str):
                request.session['is_login'] = True
                request.session['auth_type'] = 'token'
                request.session['token'] = random_str
                code = 0
                msg = '认证成功'
            else:
                code = 1
                msg = '认证文件无效！'
        res = {'code': code, 'msg': msg}
        return JsonResponse(res)


def logout(request):
    request.session.flush()
    return redirect(login)


def namespace_api(request):
    if request.method == 'GET':
        auth_type = request.session.get("auth_type")
        token = request.session.get("token")
        k8s.load_auth_config(auth_type, token)
        core_api = client.CoreV1Api()
        data = []
        try:
            for ns in core_api.list_namespace().items:
                name = ns.metadata.name
                labels = ns.metadata.labels
                create_time = ns.metadata.creation_timestamp
                namespace = {'name': name, 'labels': labels, 'create_time': create_time}
                data.append(namespace)
                code = 0
                msg = "获取数据成功"
        except Exception as e:
            code = 1
            status = getattr(e, "status")
            if status == 403:
                msg = "没有访问权限"
            else:
                msg = "获取数据失败"

        count = len(data)

        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit'))
        start = (page - 1) * limit
        end = page * limit
        data = data[start:end]

        res = {'code': code, 'msg': msg, 'count': count, 'data': data}
        return JsonResponse(res)
    elif request.method == "DELETE":
        request_data = QueryDict(request.body)
        # print(request_data)
        name = request_data.get("name")
        auth_type = request.session.get("auth_type")
        token = request.session.get("token")
        k8s.load_auth_config(auth_type, token)
        core_api = client.CoreV1Api()
        data = []
        try:
            core_api.delete_namespace(name)
            code = 0
            msg = "删除成功"
        except Exception as e:
            code = 1
            status = getattr(e, "status")
            if status == 403:
                msg = "没有删除权限！"
            else:
                msg = "删除失败！"
        res = {'code': code, 'msg': msg}
        return JsonResponse(res)


def namespace(request):
    return render(request, 'k8s/namespace.html')
