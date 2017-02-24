from django.views.generic import TemplateView, UpdateView, DetailView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.html import escape, escapejs
from django.apps import apps
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django import forms

from .models import Ingredient, IngredientSubcategory, IngredientCategory, IngredientClass
from .models import Distillery, Manufacturer
from .forms import IngredientForm


# -----------------------
# Class Based View Mixins
# -----------------------
class CreateUpdateMixin(object):
    ''' Hybrid create/update view. The get_object function is overloaded
    to return None when there is no valid object (i.e. for the Create form).
    A side effect is that, if pk returns an invalid object, the create form
    will show up instead of a 404 page.
    '''

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except AttributeError:
            return None


class PopupEditMixin(object):
    ''' This mixin overrides the get_context_data and post methods in order
    to support opening and saving popup forms in the style of the Django admin.
    '''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_name'] = self.model._meta.verbose_name.title()
        if '_popup' in self.request.GET:
            context['popup'] = self.request.GET['_popup']
        return context

    def post(self, request, *args, **kwargs):
        post_result = super().post(request, *args, **kwargs)

        if '_popup' in request.POST:
            response = '<script type="text/javascript">'
            response += 'opener.dismissAddAnotherPopup(window, "%s", "%s");' \
                % (escape(self.object.pk), escapejs(self.object))
            response += '</script>'
            return HttpResponse(response)
        else:
            return post_result


class ShortDescriptionMixin(object):
    ''' This mixin shortens the widget for the description field's Textarea '''

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if 'description' in form.fields:
            form.fields['description'].widget = forms.Textarea(attrs={'rows': 2})
        return form


class IngredientForeignKeyView(CreateUpdateMixin, PopupEditMixin, ShortDescriptionMixin, UpdateView):
    ''' Single class which handles mixins for all child classes that use an edit popup '''
    template_name = 'cocktails/ingredient_foreign_key_edit.html'


# ---------
# Home page
# ---------
class Home(TemplateView):
    template_name = 'cocktails/home.html'


# ----------
# Ingredient
# ----------
class IngredientDetail(DetailView):
    model = Ingredient


class IngredientEdit(CreateUpdateMixin, UpdateView):
    model = Ingredient
    template_name = 'cocktails/ingredient_edit.html'
    form_class = IngredientForm


# ------------------------
# Ingredient Field Classes
# ------------------------
class IngredientCategorization(TemplateView):
    ''' This view provides a single interface for looking up ingredient class,
    category and subcategory.

    At initial load, it provides a list of all classes (which in turn can be
    queried for all categories and subcategories)

    It also responds to AJAX GET requests to serve up a
    given instance of one of the three classes for viewing.
    '''

    template_name = 'cocktails/ingredient_categorization_browser.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredientclasses'] = IngredientClass.objects.all()
        return context

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            status = 200
            pk = request.GET.get('pk')
            model_type = request.GET.get('model_type')

            try:
                model = apps.get_model('cocktails', model_type)
                response = serializers.serialize('json', model.objects.filter(pk=pk), use_natural_foreign_keys=False)

            except Exception as e:
                status = 400
                response = [{'error_name': type(e).__name__, 'error-text': str(e)}]

            return HttpResponse(response, content_type="application/json", status=status)
        else:
            return super().get(request, *args, **kwargs)


class IngredientClassCreate(CreateUpdateMixin, ShortDescriptionMixin, UpdateView):
    ''' Modal class creation form '''
    model = IngredientClass
    fields = ['name', 'description', 'image_url', 'wiki_url']
    template_name = 'cocktails/ingredient_class_create.html'

    def form_valid(self, form):
        ''' Return a JSON response with the pk and a success message '''
        instance = form.save()
        message = 'New object created successfully.'
        response = {'success': 1, 'message': message, 'pk': instance.pk}
        return JsonResponse(response)

    def form_invalid(self, form):
        message = 'Object could not be created. Please resolve any errors and submit again.'
        response = {'success': 0, 'message': message, 'errors': form.errors}
        return JsonResponse(response)


class IngredientClassDetail(DetailView):
    model = IngredientClass
    template_name = 'cocktails/ingredient_class_detail.html'


class IngredientClassEdit(IngredientForeignKeyView):
    model = IngredientClass
    fields = ['name', 'description', 'image_url', 'wiki_url']


class IngredientCategoryDetail(DetailView):
    model = IngredientCategory


class IngredientCategoryEdit(IngredientForeignKeyView):
    model = IngredientCategory
    fields = ['name', 'ingredient_class', 'description', 'image_url', 'wiki_url']


class IngredientSubcategoryDetail(DetailView):
    model = IngredientSubcategory


class IngredientSubcategoryEdit(IngredientForeignKeyView):
    model = IngredientSubcategory
    fields = ['name', 'category', 'description', 'image_url', 'wiki_url']


class DistilleryDetail(DetailView):
    model = Distillery


class DistilleryEdit(IngredientForeignKeyView):
    model = Distillery
    fields = ['name', 'description', 'country', 'us_state', 'city', 'image_url', 'wiki_url', 'own_url']


class ManufacturerDetail(DetailView):
    model = Manufacturer


class ManufacturerEdit(IngredientForeignKeyView):
    model = Manufacturer
    fields = ['name', 'description', 'country', 'us_state', 'city', 'image_url', 'wiki_url', 'own_url']
