# Generated by Django 4.2 on 2023-04-11 13:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0013_alter_category_options_courses_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='course', to=settings.AUTH_USER_MODEL, verbose_name='Автор курса'),
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_entry', models.DateField(verbose_name='Дата вступления')),
                ('mark', models.IntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=10)], verbose_name='Оценка')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courses', verbose_name='Курс')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Студент')),
            ],
        ),
    ]
