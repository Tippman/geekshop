# Generated by Django 2.2.17 on 2021-01-16 12:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_auto_20210116_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 18, 12, 15, 27, 870170, tzinfo=utc)),
        ),
    ]
