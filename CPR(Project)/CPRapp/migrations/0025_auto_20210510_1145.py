# Generated by Django 3.0 on 2021-05-10 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CPRapp', '0024_auto_20210510_1112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='problem',
            old_name='location',
            new_name='doorno',
        ),
    ]