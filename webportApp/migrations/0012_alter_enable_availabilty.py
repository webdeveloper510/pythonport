# Generated by Django 3.2.3 on 2021-05-21 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webportApp', '0011_alter_enable_availabilty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enable',
            name='availabilty',
            field=models.CharField(default='', max_length=100),
        ),
    ]
