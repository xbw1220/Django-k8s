from django.shortcuts import render


# Create your views here.
def service(request):
    return render(request, 'loadbalancer/service.html')


def ingress(request):
    return render(request, 'loadbalancer/ingress.html')
