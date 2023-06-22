# Generated by Django 4.2 on 2023-06-11 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=300, verbose_name='Рвздел')),
            ],
            options={
                'verbose_name': 'Раздел форума',
                'verbose_name_plural': 'Разделы форума',
            },
        ),
        migrations.CreateModel(
            name='ForumSubsection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsection', models.CharField(max_length=300, verbose_name='Тема')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.forumsection', verbose_name='Раздел')),
            ],
            options={
                'verbose_name': 'Тема форума',
                'verbose_name_plural': 'Разделы форума',
            },
        ),
        migrations.DeleteModel(
            name='Forum',
        ),
    ]