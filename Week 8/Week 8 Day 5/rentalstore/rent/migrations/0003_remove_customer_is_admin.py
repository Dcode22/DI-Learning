# Generated by Django 3.1.2 on 2020-10-01 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0002_auto_20201001_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='is_admin',
        ),
    ]
