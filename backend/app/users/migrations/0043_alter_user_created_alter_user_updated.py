# Generated by Django 4.0.1 on 2022-04-21 13:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_alter_user_created_alter_user_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 13, 4, 52, 296251, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 21, 13, 4, 52, 296288, tzinfo=utc)),
        ),
    ]