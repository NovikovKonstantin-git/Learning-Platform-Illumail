# Generated by Django 4.2 on 2023-06-15 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0033_answermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='Вопрос')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.goodtestmodel', verbose_name='Название теста')),
            ],
        ),
        migrations.AlterField(
            model_name='answermodel',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.questionmodel', verbose_name='Вопрос'),
        ),
    ]