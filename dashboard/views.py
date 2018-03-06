from django.shortcuts import render
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth import logout


@login_required(login_url='login')
def index(request):
    return render(request, 'dashboard/index.html', context=None)

def logout(request):
    logout(request)
    return render(request,'registration/login.html', context=None)
