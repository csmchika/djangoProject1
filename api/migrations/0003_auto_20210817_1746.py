# Generated by Django 3.2.6 on 2021-08-17 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210817_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='calories',
        ),
        migrations.AddField(
            model_name='type',
            name='calories_per_km',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='activity',
            name='distance',
            field=models.FloatField(blank=True),
        ),
    ]
