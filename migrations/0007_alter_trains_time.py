# Generated by Django 4.0.5 on 2022-06-06 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_auto_20200608_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trains',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
