# Generated by Django 3.2.13 on 2022-04-22 15:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20220422_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='abouthome',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 22, 15, 10, 17, 785671, tzinfo=utc)),
        ),
    ]
