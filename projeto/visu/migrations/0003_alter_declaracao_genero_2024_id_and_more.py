# Generated by Django 4.2.17 on 2024-12-18 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visu', '0002_faixa_etaria_2024_declaracao_genero_2024_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='declaracao_genero_2024',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='declaracao_raca_2024',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
