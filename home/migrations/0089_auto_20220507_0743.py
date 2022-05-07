# Generated by Django 2.2.28 on 2022-05-07 07:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0088_auto_20220507_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abouthome',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 7, 7, 43, 5, 324191, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 7, 7, 43, 5, 339377, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 7, 7, 43, 5, 342982, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='expertise',
            name='createDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 7, 7, 43, 5, 340298, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 7, 7, 43, 5, 327267, tzinfo=utc)),
        ),
    ]