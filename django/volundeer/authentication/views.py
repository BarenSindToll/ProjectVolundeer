# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.views.generic import View
from django.shortcuts import render
from .forms import UserForm, VolunteerRegisterForm, AccRegisterForm

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

def register_user(request):
    form = VolunteerRegisterForm(data=request.POST or None)
    acc_form = AccRegisterForm(data=request.POST or None)
    errors = []
    if request.method == 'POST':
        if form.is_valid() == True and acc_form.is_valid() == True:
            form.instance.set_password(form.cleaned_data['password'])
            form.save()
            acc_form.instance.user = form.instance
            acc_form.save()
            user = authenticate(username=form.instance.username,
                                password=form.cleaned_data['password'])
            login_user(request, user)
        else:
            form = VolunteerRegisterForm(data=request.POST or None)
            acc_form = AccRegisterForm(data=request.POST or None)
            return render(request, 'register.html', {'form':form,'errors': errors})
    return render(request, "register.html", {
        'form': form,
        'acc_form' : acc_form,
        'errors': errors
    })