# Generated by Django 3.1.3 on 2020-12-20 19:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20201218_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addjob',
            name='dateposted',
            field=models.DateTimeField(default=datetime.date(2020, 12, 20)),
        ),
    ]
