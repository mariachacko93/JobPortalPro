# Generated by Django 3.1.3 on 2020-12-12 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20201212_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='employerprofile',
            name='password',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='employerprofile',
            name='job_details',
            field=models.TextField(max_length=350),
        ),
    ]