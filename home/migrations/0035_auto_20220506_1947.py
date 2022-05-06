# Generated by Django 2.2.28 on 2022-05-06 19:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_auto_20220506_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abouthome',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 19, 47, 11, 584001, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 19, 47, 11, 586601, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 19, 47, 11, 588212, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expertise',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 19, 47, 11, 587332, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 19, 47, 11, 584884, tzinfo=utc)),
        ),
    ]