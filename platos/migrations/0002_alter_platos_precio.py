# Generated by Django 4.2.1 on 2023-05-19 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platos',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]