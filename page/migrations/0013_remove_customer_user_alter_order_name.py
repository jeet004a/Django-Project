# Generated by Django 4.2 on 2023-05-16 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0012_alter_order_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]
