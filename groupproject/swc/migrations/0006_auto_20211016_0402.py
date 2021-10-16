# Generated by Django 3.2.5 on 2021-10-16 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swc', '0005_auto_20211016_0350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor_name', models.CharField(max_length=50)),
                ('logo_url', models.URLField()),
                ('sponsor_tier', models.CharField(choices=[('PL', 'PLATNIUM'), ('G', 'GOLD'), ('S', 'SILVER'), ('B', 'BRONZE')], max_length=5)),
            ],
        ),
        migrations.AlterField(
            model_name='location',
            name='state',
            field=models.CharField(choices=[('WA', 'WESTERN AUST'), ('NT', 'NORTHERN TERRITORY'), ('ACT', 'AUST CAPITAL TERRITORY'), ('SA', 'SOUTH AUST'), ('NSW', 'NEW SOUTH WALES'), ('VIC', 'VICTORIA'), ('EXT', 'EXTERNAL TERRITORIES')], max_length=5),
        ),
        migrations.AlterField(
            model_name='participant',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('N', 'Non-Binary'), ('O', 'Other')], max_length=5),
        ),
    ]