# Generated by Django 2.1.2 on 2018-11-19 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20181119_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='gallery/temp'),
        ),
    ]