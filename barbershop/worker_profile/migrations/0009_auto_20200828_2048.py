# Generated by Django 2.2 on 2020-08-28 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker_profile', '0008_auto_20200828_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerprofile',
            name='type',
            field=models.CharField(choices=[('Facebook id', 'Facebook id'), ('Instagram id', 'Instagram id'), ('Other id', 'Other id')], default=None, max_length=50),
        ),
    ]
