# Generated by Django 3.0 on 2021-04-20 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPRapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=200)),
                ('aadharno', models.CharField(max_length=200)),
                ('password', models.EmailField(default=20, max_length=254)),
                ('city', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('email', models.EmailField(default=20, max_length=254)),
                ('contactno', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default=20, max_length=254),
        ),
    ]