from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import new_order_follower, order_history, admin_panel

#Url redirection to use the views for specific paths
urlpatterns = [
    path('', views.index, name='index'),
    path('order/', new_order_follower.as_view(), name='neworder'),
    path('history/', order_history.as_view(), name='orderhistory'),
    path('admin2/', admin_panel.as_view(), name='admin_panel'),
    # path('old_history/', views.orderhistory, name='orderhistory'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile', views.profile, name='profile'),
]
#Media directory for DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
