# Generated by Django 2.2.24 on 2024-08-12 00:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_auto_20240805_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='claims', to=settings.AUTH_USER_MODEL, verbose_name='Кто пожаловался'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(related_name='owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
