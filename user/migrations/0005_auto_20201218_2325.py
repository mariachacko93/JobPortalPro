# Generated by Django 3.1.3 on 2020-12-18 19:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20201218_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addjob',
            name='dateposted',
            field=models.DateField(default=datetime.date(2020, 12, 18)),
        ),
    ]
