# Generated by Django 4.1.6 on 2023-02-27 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_courses_time_create_courses_time_update_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'ordering': ['time_create'], 'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
    ]
