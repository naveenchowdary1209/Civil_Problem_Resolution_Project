# Generated by Django 3.0 on 2021-05-13 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPRapp', '0036_auto_20210512_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='improfile',
            name='profilepic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]