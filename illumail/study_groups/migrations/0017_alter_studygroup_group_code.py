# Generated by Django 4.2 on 2023-05-22 09:29

from django.db import migrations, models
import study_groups.rand_code


class Migration(migrations.Migration):

    dependencies = [
        ('study_groups', '0016_alter_studygroup_group_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studygroup',
            name='group_code',
            field=models.CharField(default=study_groups.rand_code.generate_alphanum_crypt_string, max_length=10, unique=True, verbose_name='Код группы'),
        ),
    ]