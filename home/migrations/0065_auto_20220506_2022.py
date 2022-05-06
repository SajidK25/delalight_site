# Generated by Django 2.2.28 on 2022-05-06 20:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0064_auto_20220506_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abouthome',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 20, 22, 10, 46730, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 20, 22, 10, 49317, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 20, 22, 10, 51010, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expertise',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 20, 22, 10, 49973, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 20, 22, 10, 47634, tzinfo=utc)),
        ),
    ]
