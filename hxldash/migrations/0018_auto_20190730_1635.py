# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-07-30 16:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hxldash', '0017_auto_20190730_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='datatable',
            name='dataSource',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dashboardconfig',
            name='dataTable',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hxldash.DataTable'),
        ),
        migrations.AlterField(
            model_name='tablefield',
            name='dataTable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tableField', to='hxldash.DataTable'),
        ),
    ]
