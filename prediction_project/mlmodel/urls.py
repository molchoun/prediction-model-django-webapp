from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('form/', views.form_view, name='form'),
]