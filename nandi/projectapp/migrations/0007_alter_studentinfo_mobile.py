# Generated by Django 3.2.10 on 2022-01-09 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0006_auto_20220108_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='Mobile',
            field=models.IntegerField(),
        ),
    ]
