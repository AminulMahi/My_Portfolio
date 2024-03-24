from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from admin_app.models import Signup
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


from django.utils import timezone
from datetime import datetime, timedelta

def login(request):
    if 'user_id' in request.session:
        return redirect('admin')
    
    return render(request, 'login.html')

def logout(request):
    if 'user_id' in request.session:
        request.session.flush()
    return redirect('login')

def autolog_out(request):
    messages.success(request, 'You have been logged out due to inactivity.')
    if 'user_id' in request.session:
        request.session.flush()
    return redirect('login')

def login_user(request):
    email = request.POST.get('email')
    password = request.POST.get('pw')

    try:
        check = Signup.objects.get(email=email, password=password)
        request.session['user_id'] = check.id
        request.session['user_name'] = check.name

        return redirect('admin')
    except ObjectDoesNotExist:
        return redirect('login')












