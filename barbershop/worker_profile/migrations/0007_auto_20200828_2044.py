# Generated by Django 2.2 on 2020-08-28 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker_profile', '0006_auto_20200828_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='workerprofile',
            name='facebook_id',
            field=models.CharField(default=1, max_length=50),
        ),
        migrations.AddField(
            model_name='workerprofile',
            name='instagram_id',
            field=models.CharField(default=1, max_length=50),
        ),
        migrations.AddField(
            model_name='workerprofile',
            name='other_id',
            field=models.CharField(default=1, max_length=50),
        ),
    ]
