# Generated by Django 3.1.5 on 2021-01-21 18:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0016_auto_20210116_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 23, 18, 7, 36, 741536, tzinfo=utc)),
        ),
    ]