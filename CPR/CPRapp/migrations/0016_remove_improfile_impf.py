# Generated by Django 3.0 on 2021-04-24 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CPRapp', '0015_auto_20210424_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='improfile',
            name='impf',
        ),
    ]