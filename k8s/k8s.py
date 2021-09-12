from kubernetes import client, config
from django.shortcuts import redirect
import os


def login_auth_type(auth_type, str):
    if auth_type == 'token':
        token = str
        configuration = client.Configuration()
        configuration.host = "https://192.168.100.10:6443"
        # configuration.ssl_ca_cert = r"C:\Users\xbw12\PycharmProjects\k8s\ca.crt"
        configuration.ssl_ca_cert = r"%s" % (os.path.join("kubeconfig", "ca.crt"))
        configuration.verify_ssl = True
        configuration.api_key = {"authorization": "Bearer " + token}
        client.Configuration.set_default(configuration)
        # try:
        #     core_api = client.CoreApi()
        #     core_api.get_api_versions()  # 随便拆寻个资源测试
        #     return True
        # except Exception:
        #     return False
    elif auth_type == 'kubeconfig':
        random_str = str
        file_path = os.path.join('kubeconfig', random_str)
        config.load_kube_config(r"%s" % file_path)
        # try:
        #     core_api = client.CoreApi()
        #     core_api.get_api_versions()  # 随便拆寻个资源测试
        #     return True
        # except Exception:
        #     return False


def auth_check(auth_type, str):
    if auth_type == 'token':
        login_auth_type(auth_type, str)
        try:
            core_api = client.CoreApi()
            core_api.get_api_versions()  # 随便寻个资源测试
            return True
        except Exception:
            return False
    elif auth_type == 'kubeconfig':
        login_auth_type(auth_type, str)
        try:
            core_api = client.CoreApi()
            core_api.get_api_versions()  # 随便寻个资源测试
            return True
        except Exception:
            return False


def self_login_required(func):
    def inner(request, *args, **kwargs):
        is_login = request.session.get('is_login', False)
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return redirect("/login")

    return inner


# 加载对应认证类型的配置
def load_auth_config(auth_type, str):
    if auth_type == 'token':
        token = str
        configuration = client.Configuration()
        configuration.host = "https://192.168.100.10:6443"
        configuration.ssl_ca_cert = r"C:\Users\xbw12\PycharmProjects\k8s\ca.crt"
        configuration.verify_ssl = True
        configuration.api_key = {"authorization": "Bearer " + token}
        client.Configuration.set_default(configuration)
    elif auth_type == 'kubeconfig':
        random_str = str
        file_path = os.path.join('kubeconfig', random_str)
        config.load_kube_config(r"%s" % file_path)
