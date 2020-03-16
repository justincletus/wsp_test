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
from mtest import views as mtest_view
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'skill_test', mtest_view.SkillViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^$', mtest_view.index, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('accounts/profile/', login_view.profile, name='profile'),
    path('signup/', reg_view.signup, name='signup'),
    path('sent/', reg_view.activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', reg_view.activate, name="activate"),
    path('tests/', mtest_view.testList, name="test_list"),
    re_path(r'^test/(?P<pk>\d+)$', mtest_view.testQuestions, name="test_detail"),
    re_path(r'^', include(router.urls)),
    re_path('api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    path('test_cate/', mtest_view.testCategory, name="testcate"),
    path('submitted-test/', mtest_view.submittedTest, name="submitted_test"),
    
]
