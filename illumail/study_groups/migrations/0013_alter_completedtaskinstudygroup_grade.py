# Generated by Django 4.2 on 2023-05-21 20:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_groups', '0012_alter_completedtaskinstudygroup_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedtaskinstudygroup',
            name='grade',
            field=models.IntegerField(default='0', validators=[django.core.validators.MaxValueValidator(limit_value=10)], verbose_name='Оценка'),
        ),
    ]
