# Generated by Django 4.2 on 2023-05-28 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0014_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
