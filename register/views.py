from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:  #비밀번호와 비밀번호 확인이 일치하면
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1'],
                email=request.POST['email'],
            )
            auth.login(request, user)
            return redirect('/login') #일단 main page는 구현 안했으니 login page로
        return render(request, 'register/register.html')
    else:
        form = UserCreationForm
        return render(request, 'register/register.html', {'form':form})