from django.shortcuts import render


# Create your views here.
def node(request):
    return render(request, 'k8s/node.html')


def namespace(request):
    return render(request, 'k8s/namespace.html')


def pv(request):
    return render(request, 'k8s/pv.html')
