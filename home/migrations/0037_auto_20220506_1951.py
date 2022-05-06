# Generated by Django 2.2.28 on 2022-05-06 19:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_auto_20220506_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abouthome',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 19, 51, 55, 241891, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 19, 51, 55, 244812, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 19, 51, 55, 246569, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expertise',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 19, 51, 55, 245512, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 19, 51, 55, 242972, tzinfo=utc)),
        ),
    ]