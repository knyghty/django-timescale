# Generated by Django 3.1.4 on 2020-12-21 15:32

from django.db import migrations, models
import timescale.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', timescale.fields.TimescaleDateTimeField(interval='1 day')),
                ('temperature', models.FloatField(default=0.0)),
            ],
        ),
    ]
