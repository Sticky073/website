# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 00:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0007_auto_20170214_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientclass',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='ingredientclass',
            name='image_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Image URL'),
        ),
        migrations.AddField(
            model_name='ingredientclass',
            name='name',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingredientclass',
            name='own_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Own URL'),
        ),
        migrations.AddField(
            model_name='ingredientclass',
            name='wiki_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Wikipedia URL'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ingredients', to='cocktails.IngredientSubcategory'),
        ),
    ]
