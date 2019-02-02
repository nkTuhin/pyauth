# from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

# login functionality


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, 'You are successfully loged in')
        return redirect('index')
    else:
        contaxt = {'form': form}
    return render(request, 'login/login.html', contaxt)


# register functionality


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = UserRegisterForm()

    contaxt = {'form': form}
    return render(request, 'login/register.html', contaxt)


# logout functionality
# def logout(request):
#     return render(request, 'login/login.html')


def test_login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        messages.success(request, 'You are successfullyy loged in')
        messages.error(request, 'Password is not correct')
        login(request, user)
        return redirect('index')
    else:
        contaxt = {'form': form}
    return render(request, 'login/testlogin.html', contaxt)


def register_test_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = UserRegisterForm()

    contaxt = {'form': form}
    return render(request, 'login/testreg.jinja', contaxt)
