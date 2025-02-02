# Generated by Django 4.1.7 on 2023-02-23 08:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_measurement_sensor_alter_measurement_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='sensor',
        ),
        migrations.AddField(
            model_name='sensor',
            name='measurements',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='measurement.measurement'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 23, 8, 21, 43, 78157, tzinfo=datetime.timezone.utc)),
        ),
    ]
