# Generated by Django 3.0 on 2021-05-12 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPRapp', '0033_member_mimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mimage',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]