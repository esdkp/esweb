# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0002_auto_20141022_0506'),
    ]

    operations = [
        migrations.CreateModel(
            name='EQExpansion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.TextField()),
                ('short_name', models.TextField()),
            ],
            options={
                'verbose_name': 'Expansion',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EQFlag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('expansion', models.ForeignKey(to='roster.EQExpansion', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Flag',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='eqcharacter',
            options={'verbose_name': 'Character'},
        ),
        migrations.AlterModelOptions(
            name='eqclass',
            options={'verbose_name': 'Class', 'verbose_name_plural': 'Classes'},
        ),
        migrations.AlterModelOptions(
            name='eqrace',
            options={'verbose_name': 'Race'},
        ),
        migrations.AddField(
            model_name='eqcharacter',
            name='flags',
            field=models.ManyToManyField(to='roster.EQFlag'),
            preserve_default=True,
        ),
    ]
