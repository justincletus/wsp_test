"""wsptest_share URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import re_path, url
from django.contrib.auth import views as auth_views
from login_app import views as login_view
from app_registration import views as reg_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('accounts/profile/', login_view.profile, name='profile'),
    path('signup/', reg_view.signup, name='signup'),
    path('sent/', reg_view.activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', reg_view.activate, name="activate"),
]
