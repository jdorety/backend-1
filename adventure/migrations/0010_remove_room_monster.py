# Generated by Django 3.0.3 on 2020-02-05 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0009_auto_20200205_0229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='monster',
        ),
    ]
