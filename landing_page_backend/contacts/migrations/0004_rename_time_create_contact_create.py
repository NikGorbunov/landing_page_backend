# Generated by Django 4.1 on 2022-09-05 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_alter_contact_time_create'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='time_create',
            new_name='create',
        ),
    ]
