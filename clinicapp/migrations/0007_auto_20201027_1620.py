# Generated by Django 3.0.8 on 2020-10-27 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinicapp', '0006_auto_20201027_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='result',
            field=models.CharField(choices=[('None', 'None'), ('Negative', 'Negative'), ('Positive', 'Positive')], max_length=60),
        ),
    ]