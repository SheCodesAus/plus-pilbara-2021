# Generated by Django 3.2.5 on 2021-10-27 08:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('swc', '0002_auto_20211026_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completion_status',
            name='commencement_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 27, 8, 28, 54, 561636, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='completion_status',
            name='completion_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 27, 8, 28, 54, 561636, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 27, 8, 28, 54, 561636, tzinfo=utc)),
        ),
    ]
