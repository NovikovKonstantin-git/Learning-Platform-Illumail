# Generated by Django 4.2 on 2023-05-09 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_customuser_followers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='followers',
            new_name='subscriptions',
        ),
    ]
