# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.views.generic import View
from django.shortcuts import render
from .forms import UserForm

def login_user(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        errors = []
        form = UserForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                if user is not None:
                    login(request,user)
                    return redirect('/')
                else:
                    errors.append('Invalid username or password')
            else:
                errors.append('Form is not valid')
        return render(request, 'login.html', {'form':form,'errors': errors})

def logout_user(request):
    logout(request)
    return redirect('/')
