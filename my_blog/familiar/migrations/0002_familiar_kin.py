# Generated by Django 4.1.2 on 2022-10-18 05:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('familiar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='kin',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]
