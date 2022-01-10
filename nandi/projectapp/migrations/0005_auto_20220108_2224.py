# Generated by Django 3.2.10 on 2022-01-08 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0004_alter_employee_employeeid'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAcademics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mathsmarks', models.IntegerField(max_length=4)),
                ('Physicsmarks', models.IntegerField(max_length=4)),
                ('Chemistrymarks', models.IntegerField(max_length=4)),
                ('Biologymarks', models.IntegerField(max_length=4)),
                ('Englishmarks', models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('Rollno', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('Class', models.CharField(max_length=50)),
                ('School', models.CharField(max_length=100)),
                ('Mobile', models.IntegerField(max_length=10)),
                ('Address', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AddField(
            model_name='studentacademics',
            name='Rollno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.studentinfo'),
        ),
    ]