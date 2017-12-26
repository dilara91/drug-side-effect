"""adverseeffects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf.urls import include, url
from django.contrib import admin
from main import views
from main.views import  HomePageView
admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('login/', auth_views.login, {'template_name': 'login.html'} ,name='login'),
    path('logout/', auth_views.logout, {'template_name': 'logged_out.html'} ,name='logout'),
    path('search/', TemplateView.as_view(template_name='search.html'), name='search'),
    path('blog/', TemplateView.as_view(template_name='blog.html'), name='blog'),
    path('profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
]