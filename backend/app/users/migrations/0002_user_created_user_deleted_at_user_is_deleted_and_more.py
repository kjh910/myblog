# Generated by Django 4.0.1 on 2022-01-24 05:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 24, 5, 52, 10, 498215, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='user',
            name='deleted_at',
            field=models.DateTimeField(blank=True, help_text='Soft deletion date and time.', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_deleted',
            field=models.BooleanField(default=False, help_text='Mark an item deleted without actually deleting it from database. I.e, soft deletion.'),
        ),
        migrations.AddField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 24, 5, 52, 10, 498232, tzinfo=utc)),
        ),
    ]
