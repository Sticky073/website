# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 03:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0012_auto_20170302_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='own_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Own URL'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ingredients', to='cocktails.IngredientSubcategory'),
        ),
    ]
