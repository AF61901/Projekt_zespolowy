# Generated by Django 4.0.5 on 2022-07-05 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]