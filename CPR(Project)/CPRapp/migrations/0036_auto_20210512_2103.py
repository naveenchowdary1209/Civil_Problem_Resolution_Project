# Generated by Django 3.0 on 2021-05-12 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPRapp', '0035_auto_20210512_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mimage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
