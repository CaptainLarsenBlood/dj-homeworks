# Generated by Django 4.1.7 on 2023-02-23 08:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_remove_measurement_sensor_sensor_measurements_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='measurements',
        ),
        migrations.AddField(
            model_name='measurement',
            name='sensors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 23, 8, 23, 26, 679311, tzinfo=datetime.timezone.utc)),
        ),
    ]
