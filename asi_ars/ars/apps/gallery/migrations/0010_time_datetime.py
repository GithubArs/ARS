# Generated by Django 2.1.2 on 2018-12-04 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='time',
            name='datetime',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
