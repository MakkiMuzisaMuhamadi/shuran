# Generated by Django 5.0.5 on 2024-05-11 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0011_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]