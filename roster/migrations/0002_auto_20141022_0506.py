# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eqcharacter',
            name='surname',
            field=models.TextField(blank=True),
        ),
    ]
