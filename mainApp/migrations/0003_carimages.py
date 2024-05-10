# Generated by Django 5.0.5 on 2024-05-09 08:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_rename_year_cars_model_cars_date_cars_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='car_other_images/')),
                ('car', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainApp.cars')),
            ],
        ),
    ]