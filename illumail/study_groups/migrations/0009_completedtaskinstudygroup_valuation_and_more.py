# Generated by Django 4.2 on 2023-05-18 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study_groups', '0008_alter_completedtaskinstudygroup_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='completedtaskinstudygroup',
            name='valuation',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='study_groups.valuation', verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='valuation',
            name='compl_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='valuations', to='study_groups.completedtaskinstudygroup', verbose_name='Выполненное задание'),
        ),
    ]
