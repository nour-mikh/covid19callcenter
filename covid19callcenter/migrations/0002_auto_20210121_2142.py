# Generated by Django 3.1.2 on 2021-01-21 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covid19callcenter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caller',
            old_name='adress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='adress',
            new_name='address',
        ),
    ]