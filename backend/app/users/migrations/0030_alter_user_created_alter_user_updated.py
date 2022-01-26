# Generated by Django 4.0.1 on 2022-01-26 07:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_alter_user_created_alter_user_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 26, 7, 51, 49, 300104, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 26, 7, 51, 49, 300190, tzinfo=utc)),
        ),
    ]
