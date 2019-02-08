from django.contrib import admin
from users.models import order_follower, order_like, profile

# Register your models here.
admin.site.register(order_like)
admin.site.register(order_follower)
admin.site.register(profile)