from django.urls import path
from . import views

#Url redirection to use the views for specific paths
urlpatterns = [
    path('', views.neworder, name='users-home'),
    path('history/', views.orderhistory, name='orderhistory'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact')
]
