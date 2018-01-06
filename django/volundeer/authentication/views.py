# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def login_view(request):
    return render(request, 'login.html')

class UserFormView(View):
    form_class = UserForm
    template_name = 'templates/registerVoluntar.html'

    #display blank form-user with no account
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #process from data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #cleaned (normalized) data - everyone use the same letters
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('authentication:index')

    return render(request, self.template_name, {'form': form})