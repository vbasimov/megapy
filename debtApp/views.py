from django.shortcuts import render, redirect
from debtApp.forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from debtApp import grid

def index(request):
    return render(request, 'debtApp/index.html', {})

def register(request):

    userForm = UserForm()

    if request.method == 'POST':
        userForm = UserForm(request.POST)
        if userForm.is_valid():
            newUser = User.objects.create_user(**userForm.cleaned_data)
            login(request, authenticate(
                username = userForm.cleaned_data['username'],
                password = userForm.cleaned_data['password']
            ))
            return redirect(grid.debtGrid)
    return render(request, 'debtApp/register.html', {'userForm': userForm})

def error(request):
    return render(request, 'debtApp/error.html', {})
