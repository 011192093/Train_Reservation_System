# Generated by Django 4.0.5 on 2022-06-06 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0012_seats_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trains',
            name='Seat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.seats'),
        ),
    ]