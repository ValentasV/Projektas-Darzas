# Generated by Django 4.2.2 on 2023-09-05 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('augalas', '0004_alter_augalas_veisle'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='augalas',
            unique_together={('pavadinimas', 'veisle')},
        ),
    ]
