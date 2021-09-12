from django.shortcuts import render


# Create your views here.
def deployment(request):
    return render(request, 'workload/deployment.html')


def daemonset(request):
    return render(request, 'workload/daemonset.html')


def statefulset(request):
    return render(request, 'workload/statefulset.html')


def pods(request):
    return render(request, 'workload/pods.html')


def cronjobs(request):
    return render(request, 'workload/cronjobs.html')


def jobs(request):
    return render(request, 'workload/jobs.html')
