# Generated by Django 3.0 on 2021-05-12 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPRapp', '0031_auto_20210512_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='paystatus',
            field=models.TextField(default=0),
        ),
    ]