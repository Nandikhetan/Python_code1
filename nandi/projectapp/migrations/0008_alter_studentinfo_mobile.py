# Generated by Django 3.2.10 on 2022-01-09 10:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0007_alter_studentinfo_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='Mobile',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
