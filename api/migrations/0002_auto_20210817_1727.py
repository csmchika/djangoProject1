# Generated by Django 3.2.6 on 2021-08-17 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='finished',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='started',
            field=models.TimeField(blank=True),
        ),
    ]
