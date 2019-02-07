from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#Url redirection to use the views for specific paths
urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.neworder, name='neworder'),
    path('history/', views.orderhistory, name='orderhistory'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout')
]
