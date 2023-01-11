# Generated by Django 4.1.4 on 2023-01-08 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_store_condition_alter_store_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='year',
            field=models.IntegerField(choices=[(2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], verbose_name='year'),
        ),
    ]
