# Generated by Django 3.0 on 2021-05-12 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPRapp', '0032_auto_20210512_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='mimage',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
