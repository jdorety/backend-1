# Generated by Django 3.0.3 on 2020-02-05 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0006_auto_20200204_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monster',
            name='uuid',
        ),
    ]
