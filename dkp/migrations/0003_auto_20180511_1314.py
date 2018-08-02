# Generated by Django 2.0.1 on 2018-05-11 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eq', '0009_auto_20180509_2224'),
        ('dkp', '0002_auto_20180509_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='loot',
            name='character',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eq.Character'),
        ),
        migrations.AlterField(
            model_name='loot',
            name='dkp',
            field=models.FloatField(default=0),
        ),
    ]