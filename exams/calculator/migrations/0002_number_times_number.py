# Generated by Django 2.1.1 on 2019-02-14 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='number_times',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
