# Generated by Django 4.2 on 2023-05-06 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_rename_name1_tag_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date_cretaed',
            new_name='date_created',
        ),
    ]