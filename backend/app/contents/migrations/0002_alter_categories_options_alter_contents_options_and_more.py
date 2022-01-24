# Generated by Django 4.0.1 on 2022-01-24 06:00

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='contents',
            options={'verbose_name_plural': 'Contents'},
        ),
        migrations.AddField(
            model_name='contents',
            name='category',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, related_name='category', to='contents.categories'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 24, 6, 0, 38, 228296, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='category_name'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 24, 6, 0, 38, 228315, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contents',
            name='content',
            field=models.CharField(blank=True, default='', max_length=5000, verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='contents',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 24, 6, 0, 38, 228296, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contents',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 24, 6, 0, 38, 228315, tzinfo=utc)),
        ),
    ]
