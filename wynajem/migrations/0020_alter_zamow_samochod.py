# Generated by Django 4.0.5 on 2022-07-05 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wynajem', '0019_alter_zamow_data_odbioru_alter_zamow_data_oddania'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zamow',
            name='samochod',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wynajem.samochody'),
        ),
    ]
