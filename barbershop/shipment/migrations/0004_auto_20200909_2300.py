# Generated by Django 2.2 on 2020-09-09 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shipment', '0003_auto_20200907_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipment',
            name='created_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipment_shipment_created_by', to=settings.AUTH_USER_MODEL, verbose_name='Ким створено'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Коли створено'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipment',
            name='updated_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipment_shipment_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='Ким змінено'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Коли змінено'),
        ),
    ]
