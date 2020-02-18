from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html')


@login_required
def password_change_done(request):
    messages.success(request, "Пароль успешно сохранен")
    return redirect('dashboard')


# @login_required
# def add_new_chat(request):

