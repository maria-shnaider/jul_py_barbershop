# Generated by Django 2.2 on 2020-08-29 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker_profile', '0017_auto_20200829_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='workerprofile',
            name='facebook_id',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AddField(
            model_name='workerprofile',
            name='instagram_id',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AddField(
            model_name='workerprofile',
            name='other_id',
            field=models.CharField(default=None, max_length=15),
        ),
    ]
