# Generated by Django 3.0.3 on 2020-02-05 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0008_room_monster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='monster',
            field=models.IntegerField(default=0),
        ),
    ]
