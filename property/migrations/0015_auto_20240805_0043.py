# Generated by Django 2.2.24 on 2024-08-04 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20240804_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to=settings.AUTH_USER_MODEL, verbose_name='Кто пожаловался'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='property.Flat', verbose_name='Квартира на которую пожаловались'),
        ),
    ]
