# Generated by Django 3.0 on 2021-04-20 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPRapp', '0003_auto_20210420_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg',
            name='password',
        ),
        migrations.AddField(
            model_name='reg',
            name='password1',
            field=models.CharField(default=20, max_length=20),
        ),
        migrations.AddField(
            model_name='reg',
            name='password2',
            field=models.CharField(default=20, max_length=20),
        ),
    ]
