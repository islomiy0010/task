from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import *
@login_required(login_url='login-page')
def home(request):
    if request.method=='POST':
        taskValue=request.POST['task']
        data=Task(task=taskValue,user=request.user)
        data.save()
        return redirect('home-page')
    task=Task.objects.all()
    return render(request,'home.html',{'tasks':task})

def signup(request):
    if request.method=='POST':
        username=request.POST['uname']
        email=request.POST['email']
        password1=request.POST['pwd']
        password2=request.POST['pwd2']
        if User.objects.filter(username=username).exists():
            status='Bu username bilan allaqachon royxatdan otilgan'
            return render(request,'signup.html',{'status':status})
        if password1!=password2:
            status='parol va tasdiqlovchi parol mos kelmadi'
            return render(request, 'signup.html', {'status': status})
        if password1==password2:
            usr=User.objects.create_user(username=username,email=email,password=password1)
            usr.save()
            return redirect('login-page')
    return render(request,'signup.html')

def loginForm(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pwd')
        usr=authenticate(request,username=username,password=password)
        if usr is not None:
            login(request,usr)
            return redirect('home-page')
        else:
            status='username yoki parol xato'
            return render(request,'login.html',{'status':status})
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return render(request,'logout.html')

def error_404(request,exception):
    return render(request,'error_404.html')

def task_delete(request,pk):
    Task.objects.filter(id=pk).delete()
    return redirect('home-page')

def task_edit(request,pk):
    data=Task.objects.get(id=pk)
    if request.method == 'POST':
        taskValue = request.POST['task']
        Task.objects.filter(id=pk).update(task=taskValue)
        return redirect('home-page')
    return render(request,'task_edit.html',{'task':data})