# Generated by Django 3.2.2 on 2021-05-09 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(blank=True, max_length=80)),
                ('phone', models.IntegerField()),
                ('type', models.CharField(max_length=20)),
            ],
        ),
    ]
