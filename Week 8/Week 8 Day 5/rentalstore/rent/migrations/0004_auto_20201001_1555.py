# Generated by Django 3.1.2 on 2020-10-01 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_remove_customer_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=40),
        ),
    ]
