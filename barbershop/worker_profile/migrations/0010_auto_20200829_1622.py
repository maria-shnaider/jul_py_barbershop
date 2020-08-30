# Generated by Django 2.2 on 2020-08-29 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('worker_profile', '0009_auto_20200828_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='workerprofile',
            name='comm_id',
            field=models.CharField(choices=[('Facebook id', 'Facebook id'), ('Instagram id', 'Instagram id'), ('Other id', 'Other id')], default='', max_length=150),
        ),
        migrations.AddField(
            model_name='workerprofile',
            name='facebook_id',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workerprofile',
            name='instagram_id',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workerprofile',
            name='other_id',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workerprofile',
            name='profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='worker_profile.WorkerProfile'),
        ),
        migrations.AlterField(
            model_name='workerprofile',
            name='type',
            field=models.CharField(choices=[('Facebook id', 'Facebook id'), ('Instagram id', 'Instagram id'), ('Other id', 'Other id')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='workerprofile',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
