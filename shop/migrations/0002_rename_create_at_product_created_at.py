# Generated by Django 4.0 on 2022-04-22 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
