# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-08 01:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("eq", "0003_auto_20170408_0053")]

    operations = [
        migrations.AlterField(
            model_name="character",
            name="guild",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="eq.Guild",
            ),
        )
    ]
