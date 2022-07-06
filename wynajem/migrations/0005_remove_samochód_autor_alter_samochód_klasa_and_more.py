# Generated by Django 4.0.5 on 2022-06-28 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wynajem', '0004_samochód_cena_samochód_miejsca'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='samochód',
            name='autor',
        ),
        migrations.AlterField(
            model_name='samochód',
            name='klasa',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='samochód',
            name='klimatyzacja',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='samochód',
            name='model',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='samochód',
            name='paliwo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='samochód',
            name='skrzynia',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
