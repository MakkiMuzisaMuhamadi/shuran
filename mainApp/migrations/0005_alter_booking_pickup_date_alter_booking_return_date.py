# Generated by Django 5.0.5 on 2024-05-09 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='pickup_date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='return_date',
            field=models.CharField(max_length=20),
        ),
    ]
