"""wikisearch URL Configuration

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
from django.contrib import admin
from django.urls import path

from . import views

app_name = "dashboard"

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('', views.LoginView.as_view(), name='login'),
    path('index/', views.IndexView.as_view(), name="index"),
    path('blank/', views.BlankView.as_view(), name="blank"),
    path('buttons/', views.ButtonsView.as_view(), name="buttons"),
    path('flot/', views.FlotView.as_view(), name="flot"),
    path('forms/', views.FormsView.as_view(), name="forms"),
    path('grid/', views.GridView.as_view(), name="grid"),
    path('icons/', views.IconsView.as_view(), name="icons"),
    path('morris/', views.MorrisView.as_view(), name="morris"),
    path('notifications/', views.NotificationsView.as_view(), name="notifications"),
    path('panels/', views.PanelsView.as_view(), name="panels"),
    path('tables/', views.TablesView.as_view(), name="tables"),
    path('typography/', views.TypographyView.as_view(), name="typography"),
]
