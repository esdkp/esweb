# Generated by Django 2.0.1 on 2018-05-09 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dkp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loot',
            old_name='dkp_value',
            new_name='dkp',
        ),
    ]
