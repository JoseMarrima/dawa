# Generated by Django 3.0.8 on 2020-10-26 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicapp', '0002_auto_20201015_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='published_date',
        ),
        migrations.AddField(
            model_name='exam',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr_codes'),
        ),
    ]
