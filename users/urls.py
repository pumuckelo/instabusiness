from django.urls import path
from . import views

#Url redirection to use the views for specific paths
urlpatterns = [
    path('', views.index, name='index'),
    path('order/', views.neworder, name='order'),
    path('history/', views.orderhistory, name='orderhistory'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login', views.login, name='login'),
]
