# Generated by Django 3.2.5 on 2021-11-01 03:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('swc', '0007_merge_0005_auto_20211101_1144_0006_auto_20211030_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='profile_pic',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='completion_status',
            name='commencement_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 3, 54, 52, 627300, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='completion_status',
            name='completion_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 3, 54, 52, 627300, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 3, 54, 52, 629294, tzinfo=utc)),
        ),
    ]
