# Generated by Django 4.0.5 on 2022-07-05 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wynajem', '0023_remove_zamow_samochod'),
    ]

    operations = [
        migrations.AddField(
            model_name='zamow',
            name='samochod',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='wynajem.samochody'),
            preserve_default=False,
        ),
    ]
