# Generated by Django 3.2.10 on 2022-01-08 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0005_auto_20220108_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentacademics',
            name='Biologymarks',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentacademics',
            name='Chemistrymarks',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentacademics',
            name='Englishmarks',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentacademics',
            name='Mathsmarks',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='studentacademics',
            name='Physicsmarks',
            field=models.IntegerField(),
        ),
    ]
