# Generated by Django 2.0 on 2017-12-17 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0003_auto_20171217_0805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='threshold',
        ),
        migrations.AddField(
            model_name='setting',
            name='humid_threshold',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='setting',
            name='temp_threshold',
            field=models.IntegerField(default=50),
        ),
    ]
