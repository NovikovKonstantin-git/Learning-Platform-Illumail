# Generated by Django 4.2 on 2023-06-16 01:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0038_alter_courses_progress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='progress',
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(limit_value=100)], verbose_name='Прогресс')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courses', verbose_name='Курс')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Прогресс',
                'verbose_name_plural': 'Прогресс',
            },
        ),
    ]