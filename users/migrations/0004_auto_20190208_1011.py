# Generated by Django 2.1.5 on 2019-02-08 10:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_auto_20190208_1007'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='order_followers',
            new_name='order_follower',
        ),
        migrations.RenameModel(
            old_name='order_likes',
            new_name='order_like',
        ),
    ]
