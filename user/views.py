from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .forms import UserRegisterForms
from .models import MyUser


def user_register_view(request):
    if request.method == 'POST':
        form = UserRegisterForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировалитсь!')
            return redirect('index')
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f'{error}')

    form = UserRegisterForms()
    return render(request, 'account/user_register.html', {'form': form})

def user_login_view(request):
    if request.method == 'POST':
        user_email = request.POST['email']
        user_password = request.POST['password']

        user = authenticate(request, username=user_email, password=user_password)

        if user:
            login(request, user)
            messages.success(request, 'Вы успешно вошли в систему!')
            return redirect('index')
        else:
            messages.error(request, 'Неверный логин или пароль')

    return render(request, 'account/user_login.html')

def user_logout_view(request):
    logout(request)
    messages.success(request,'Вы успешно вышли из системы')
    return redirect('index')

def profile_view(request):
    user = get_object_or_404(MyUser, id=request.user.id)
    return render(request, 'account/profile.html', {'user': user})