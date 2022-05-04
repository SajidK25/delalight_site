# Generated by Django 2.2.28 on 2022-05-04 08:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name', max_length=200)),
                ('title', models.CharField(help_text='Title', max_length=200)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='uploads/')),
                ('publishedDate', models.DateTimeField(blank=True, null=True)),
                ('create_date', models.DateTimeField(default=datetime.datetime(2022, 5, 4, 8, 59, 28, 486801, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name', max_length=200)),
                ('title', models.CharField(help_text='Title', max_length=200)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('text', models.TextField(blank=True, null=True)),
                ('publishedDate', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title', max_length=200)),
                ('text', models.TextField()),
                ('createDate', models.DateTimeField(default=datetime.datetime(2022, 5, 4, 8, 59, 28, 488526, tzinfo=utc))),
                ('publishedDate', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title', max_length=200)),
                ('name', models.CharField(blank=True, help_text='Name', max_length=200, null=True)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('createDate', models.DateTimeField(default=datetime.datetime(2022, 5, 4, 8, 59, 28, 489083, tzinfo=utc))),
                ('publishedDate', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boldtext', models.TextField()),
                ('text', models.TextField()),
                ('createDate', models.DateTimeField(default=datetime.datetime(2022, 5, 4, 8, 59, 28, 488047, tzinfo=utc))),
                ('publishedDate', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AboutHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('createDate', models.DateTimeField(default=datetime.datetime(2022, 5, 4, 8, 59, 28, 486223, tzinfo=utc))),
                ('publishedDate', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
