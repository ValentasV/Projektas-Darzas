# Generated by Django 4.2.2 on 2023-09-04 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('augalas', '0004_alter_augalas_veisle'),
        ('darzas', '0002_alter_darzodarbas_pavadinimas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='darzas',
            name='augalas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='augalas.augalas', unique=True),
        ),
        migrations.AlterField(
            model_name='darzoderlius',
            name='augalas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='augalas.augalas', unique=True),
        ),
    ]
