# Generated by Django 2.0 on 2017-12-19 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0010_auto_20171218_2004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='using_setting',
            new_name='setting',
        ),
    ]