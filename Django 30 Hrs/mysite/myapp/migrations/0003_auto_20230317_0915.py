# Generated by Django 3.1 on 2023-03-17 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20230315_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_year_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_year_start',
            field=models.DateField(),
        ),
    ]
