# Generated by Django 3.1 on 2023-03-10 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField()),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='contract',
            fields=[
                ('contracte_id', models.AutoField(primary_key=True, serialize=False)),
                ('contract_no', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='owner',
            fields=[
                ('owner_id', models.AutoField(primary_key=True, serialize=False)),
                ('depcode', models.TextField(blank=True, null=True)),
                ('template', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='system_action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.TextField(null=True)),
                ('depcode', models.TextField(null=True)),
                ('readonly', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='title',
            fields=[
                ('title_id', models.AutoField(primary_key=True, serialize=False)),
                ('title_name', models.TextField(null=True)),
                ('contract_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.contract')),
            ],
        ),
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quarter_no', models.IntegerField(null=True)),
                ('data_confirm', models.TextField(null=True)),
                ('result', models.TextField(null=True)),
                ('problem', models.TextField(null=True)),
                ('solution', models.TextField(null=True)),
                ('year', models.DateField()),
                ('owner_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.owner')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('detail', models.TextField()),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.TextField()),
                ('project_year_start', models.TextField()),
                ('project_year_end', models.TextField()),
                ('User', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='owner',
            name='title_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.title'),
        ),
        migrations.AddField(
            model_name='contract',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.project'),
        ),
    ]
