# Generated by Django 3.2.2 on 2021-05-10 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_api', '0004_remove_contacts_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='created_at',
        ),
    ]
