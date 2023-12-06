# Generated by Django 4.2.7 on 2023-11-19 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('technology_used', models.CharField(default='', max_length=50)),
                ('description', models.CharField(default='', max_length=200)),
                ('roles', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='employee_project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.project')),
            ],
        ),
    ]