# Generated by Django 3.2 on 2021-04-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customer_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
