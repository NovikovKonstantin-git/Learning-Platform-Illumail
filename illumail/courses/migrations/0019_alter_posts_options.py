# Generated by Django 4.2 on 2023-05-14 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_alter_posts_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-time_created'], 'verbose_name': 'Материал курса', 'verbose_name_plural': 'Материалы курса'},
        ),
    ]