# Generated by Django 4.0.1 on 2022-01-26 08:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0034_alter_categories_created_alter_categories_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 26, 8, 10, 54, 628168, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='categories',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 26, 8, 10, 54, 628217, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contents',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 26, 8, 10, 54, 628168, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contents',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 26, 8, 10, 54, 628217, tzinfo=utc)),
        ),
    ]
