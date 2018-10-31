from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from test import test_contextlib

class UserControl():
    
    def welcome(self, request):
        return render(request, 'welcome.html')
    
    def addUser(self, request):
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid:
                form.save()
                return redirect('/userControl/login')
        else:
            form = UserCreationForm()
            context = {'form': form}
            return render(request, 'user_control_add_user.html', context) 
    
    def login(self, request):
        if request.method == "POST":
            form = AuthenticationForm(request.POST)
            if form.is_valid:
                usuario = request.POST['username']
                passwd = request.POST['password']
                acceso = authenticate(username = usuario, password = passwd )
                if acceso is not None:
                    if acceso.is_active:
                        login(request,acceso)
                        return redirect('/welcome')
                    else:
                        return redirect('/userControl/inactive/') #usuario inactivo
                else:
                    return redirect('/userControl/user_not_found/') #usuario inexistente
        else:
            form = AuthenticationForm()
            context = { 'form': form }
            return render(request, 'user_control_login.html', context)
    
    def userInactive(self, request):
        context = {}
        return render(request, 'user_control_user_inactive.html', context)
    
    def userNotFound(self, request):
        context = {}
        return render(request, 'user_control_user_not_found.html', context)
    
    @login_required(login_url="/userControl/login/")
    def deleteLogin(self, request):
        logout(request)
        return redirect('/userControl/login/')
        
                