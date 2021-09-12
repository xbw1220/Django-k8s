from django.shortcuts import render


# Create your views here.
def pvc(request):
    return render(request, 'storage/pvc.html')


def configmap(request):
    return render(request, 'storage/configmap.html')


def secret(request):
    return render(request, 'storage/secret.html')
