# Generated by Django 2.1.2 on 2018-11-19 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20181119_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Retrain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('suggested', models.CharField(max_length=30)),
                ('image', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.CharField(max_length=120),
        ),
    ]
