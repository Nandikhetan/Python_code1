# Generated by Django 3.2.10 on 2021-12-24 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('page', models.IntegerField()),
                ('pemail', models.EmailField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Edepartment', models.CharField(max_length=100)),
                ('Erole', models.CharField(max_length=100)),
                ('Employeeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reverse.person')),
            ],
        ),
    ]