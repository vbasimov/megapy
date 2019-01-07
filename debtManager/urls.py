"""debtManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from debtApp import views, api

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    #common paths
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='debtApp/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page = '/'), name = 'logout'),
    path('error', views.error, name='error'),
    path('debts/', views.debtGrid, name='debt-grid'),

    #api paths
    path('debts/api/', api.allDebts),
    path('debts/create', api.debtCreate),
    path('debts/<int:debt_id>/update', api.debtUpdate),
    path('debts/<int:debt_id>/delete', api.debtDelete)
]
