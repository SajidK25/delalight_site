# Generated by Django 2.2.28 on 2022-05-04 10:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20220504_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abouthome',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 10, 59, 39, 506037, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 10, 59, 39, 507823, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 10, 59, 39, 508809, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expertise',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 10, 59, 39, 508303, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 10, 59, 39, 506570, tzinfo=utc)),
        ),
    ]
