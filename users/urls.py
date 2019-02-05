from django.urls import path
from . import views

#Url redirection to use the views for specific paths
urlpatterns = [
    path('', views.neworder, name='users-home'),
]
