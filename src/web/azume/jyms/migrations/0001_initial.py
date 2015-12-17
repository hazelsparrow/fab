# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jym',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('lat', models.DecimalField(max_digits=21, decimal_places=18)),
                ('lng', models.DecimalField(max_digits=21, decimal_places=18)),
            ],
        ),
    ]
