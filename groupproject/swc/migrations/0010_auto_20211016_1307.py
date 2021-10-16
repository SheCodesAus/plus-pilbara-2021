# Generated by Django 3.2.5 on 2021-10-16 05:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('swc', '0009_auto_20211016_1253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='date',
            new_name='start_date',
        ),
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.ManyToManyField(to='swc.Language'),
        ),
        migrations.AddField(
            model_name='language',
            name='constraned_by',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]