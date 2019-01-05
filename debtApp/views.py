from django.shortcuts import render

def index(request):
    return render(request, 'debtApp/index.html', {})

def login(request):
    return render(request, 'debtApp/login.html', {})

def register(request):
    return render(request, 'debtApp/register.html', {})

def error(request):
    return render(request, 'debtApp/error.html', {})

def debtGrid(request):
    return render(request, 'debtApp/debt-grid.html', {})
