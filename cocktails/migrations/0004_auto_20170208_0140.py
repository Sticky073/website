# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 01:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0003_auto_20170208_0135'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tools',
            new_name='Tool',
        ),
        migrations.AlterModelOptions(
            name='cocktailcategory',
            options={'verbose_name_plural': 'cocktail categories'},
        ),
        migrations.AlterModelOptions(
            name='glassware',
            options={'verbose_name_plural': 'glassware'},
        ),
        migrations.AlterModelOptions(
            name='ingredientclass',
            options={'verbose_name_plural': 'ingredient classes'},
        ),
        migrations.AlterModelOptions(
            name='unitofmeasure',
            options={'verbose_name_plural': 'units of measure'},
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ingredients', to='cocktails.IngredientSubcategory'),
        ),
    ]