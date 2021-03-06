# Generated by Django 4.0.1 on 2022-01-26 05:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0014_alter_categories_created_alter_categories_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 26, 5, 15, 25, 646290, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='categories',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 26, 5, 15, 25, 646311, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contents',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 26, 5, 15, 25, 646290, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contents',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 26, 5, 15, 25, 646311, tzinfo=utc)),
        ),
    ]
