# Generated by Django 4.2 on 2023-04-05 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_alter_completedtaskmodel_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='completedtaskmodel',
            options={'ordering': ['-time_load'], 'verbose_name': 'Выполненное задание', 'verbose_name_plural': 'Выполненные задания'},
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-time_created'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]