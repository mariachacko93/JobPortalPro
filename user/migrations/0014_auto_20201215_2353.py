# Generated by Django 3.1.3 on 2020-12-15 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20201215_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addjob',
            name='date_posted',
            field=models.DateField(default='YYYY-MM-DD'),
        ),
    ]
