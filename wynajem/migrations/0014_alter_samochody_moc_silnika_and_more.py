# Generated by Django 4.0.5 on 2022-07-04 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wynajem', '0013_samochody_moc_silnika_samochody_nadwozie_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samochody',
            name='moc_silnika',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='samochody',
            name='pojemnosc_silnika',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='samochody',
            name='spalanie_miasto',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='samochody',
            name='spalanie_trasa',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
