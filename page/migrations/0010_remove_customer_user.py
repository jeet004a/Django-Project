# Generated by Django 4.2 on 2023-05-15 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0009_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
