# Generated by Django 4.2 on 2023-04-04 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_options_alter_customuser_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.CharField(default='О себе...', max_length=200, verbose_name='О себе'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Фото'),
        ),
    ]
