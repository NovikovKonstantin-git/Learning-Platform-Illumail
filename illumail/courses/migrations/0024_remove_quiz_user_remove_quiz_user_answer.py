# Generated by Django 4.2 on 2023-05-25 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0023_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='user',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='user_answer',
        ),
    ]
