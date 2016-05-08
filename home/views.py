# -*- coding: utf-8 -*-

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

from .forms import UserForm

@login_required
def home_page(request):
    context = {}
    return render(request,"home.html",context)

def login_view(request,in_errMessage=None):
    if request.method == 'GET':
        login_form = UserForm()
        if request.user.is_authenticated():
            return redirect("/")
        context={'login_form':login_form}
        if in_errMessage is not None:
            context['login_error'] = in_errMessage
        return render(request,"login.html",context)
    elif request.method == 'POST':
        login_form = UserForm()
        if request.user.is_authenticated():
            return redirect("/")
        context = {}
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:     
                request.session['username'] = username
                login(request, user)
                return redirect("/")
            else:
                context['login_form'] = login_form
                context['login_error'] = "Ovaj nalog je neaktivan!"
                return render(request,'login.html',context)           
        else:    
            context['login_form'] = login_form
            context['login_error'] = "Netačno korisničko ime i/ili šifra!"
            return render(request,'login.html',context)
    else:
        print "ERROR"
        
@login_required
def logout_view(request,in_errMessage=None):
    logout(request)
    return login_view(request,in_errMessage)
