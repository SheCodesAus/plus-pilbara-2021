# Generated by Django 3.2.5 on 2021-11-01 04:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('swc', '0007_auto_20211101_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completion_status',
            name='commencement_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 4, 0, 18, 387162, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='completion_status',
            name='completion_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 4, 0, 18, 387178, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 4, 0, 18, 387911, tzinfo=utc)),
        ),
    ]