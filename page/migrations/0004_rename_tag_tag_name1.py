# Generated by Django 4.2 on 2023-05-06 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_tag_order_customer_order_product_product_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='Tag',
            new_name='name1',
        ),
    ]
