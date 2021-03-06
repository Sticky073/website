# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 00:03
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0006_auto_20170208_0207'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='distillery',
            options={'verbose_name_plural': 'distilleries'},
        ),
        migrations.AlterModelOptions(
            name='ingredientcategory',
            options={'verbose_name_plural': 'ingredient categories'},
        ),
        migrations.AlterModelOptions(
            name='ingredientsubcategory',
            options={'verbose_name_plural': 'ingredient subcategories'},
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='average_cost',
        ),
        migrations.RemoveField(
            model_name='ingredientclass',
            name='description',
        ),
        migrations.RemoveField(
            model_name='ingredientclass',
            name='name',
        ),
        migrations.AddField(
            model_name='cocktail',
            name='own_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Own URL'),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='wiki_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Wikipedia URL'),
        ),
        migrations.AddField(
            model_name='cocktailcategory',
            name='image_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Image URL'),
        ),
        migrations.AddField(
            model_name='cocktailcategory',
            name='own_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Own URL'),
        ),
        migrations.AddField(
            model_name='cocktailcategory',
            name='wiki_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Wikipedia URL'),
        ),
        migrations.AddField(
            model_name='distillery',
            name='image_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Image URL'),
        ),
        migrations.AddField(
            model_name='distillery',
            name='own_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Own URL'),
        ),
        migrations.AddField(
            model_name='glassware',
            name='own_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Own URL'),
        ),
        migrations.AddField(
            model_name='glassware',
            name='wiki_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Wikipedia URL'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='own_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Own URL'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='wiki_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Wikipedia URL'),
        ),
        migrations.AddField(
            model_name='ingredientcategory',
            name='own_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Own URL'),
        ),
        migrations.AddField(
            model_name='ingredientcategory',
            name='wiki_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Wikipedia URL'),
        ),
        migrations.AddField(
            model_name='ingredientsubcategory',
            name='own_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Own URL'),
        ),
        migrations.AddField(
            model_name='ingredientsubcategory',
            name='wiki_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Wikipedia URL'),
        ),
        migrations.AddField(
            model_name='manufacturer',
            name='image_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Image URL'),
        ),
        migrations.AddField(
            model_name='preparationmethod',
            name='image_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Image URL'),
        ),
        migrations.AddField(
            model_name='preparationmethod',
            name='own_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Own URL'),
        ),
        migrations.AddField(
            model_name='preparationmethod',
            name='wiki_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Wikipedia URL'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='own_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Own URL'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='wiki_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Wikipedia URL'),
        ),
        migrations.AddField(
            model_name='tool',
            name='own_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Own URL'),
        ),
        migrations.AddField(
            model_name='tool',
            name='wiki_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Wikipedia URL'),
        ),
        migrations.AlterField(
            model_name='cocktail',
            name='image_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='cocktailcategory',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='cocktailcategory',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='distillery',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='glassware',
            name='image_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='abv',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.00')), django.core.validators.MaxValueValidator(Decimal('100.00'))]),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='image_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ingredients', to='cocktails.IngredientSubcategory'),
        ),
        migrations.AlterField(
            model_name='ingredientcategory',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='ingredientcategory',
            name='image_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='ingredientcategory',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='ingredientsubcategory',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='ingredientsubcategory',
            name='image_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='ingredientsubcategory',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='own_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Own URL'),
        ),
        migrations.AlterField(
            model_name='preparationmethod',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='preparationmethod',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='tool',
            name='image_url',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Image URL'),
        ),
    ]
