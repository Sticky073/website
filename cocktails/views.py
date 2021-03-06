from django.views.generic import TemplateView, UpdateView
from django.utils.html import escape, escapejs
from django.apps import apps
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django import forms

from .models import Ingredient, IngredientSubcategory, IngredientCategory, IngredientClass
from .models import Brand, Distillery, Manufacturer
from .models import Cocktail, CocktailCategory
from .forms import IngredientForm, BrandForm, CocktailForm


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


class JsonFormMixin(object):
    ''' This mixin provides Json responses for the form_valid and form_invalid
    methods, allowing forms to be posted asynchronously.
    '''

    def get(self, request, *args, **kwargs):
        ''' Improve get so we can load the form with initial values and
        respond to AJAX requests.
        '''
        if request.is_ajax():
            return self.ajax_handler(request)

        else:
            return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        ''' Return a JSON response with the pk and a success message '''
        instance = form.save()
        response = {'success': 1, 'pk': instance.pk, 'detail_url': instance.get_absolute_url()}
        return JsonResponse(response)

    def form_invalid(self, form):
        response = {'success': 0, 'errors': form.errors}
        return JsonResponse(response)

    def verbose_name(self):
        return self.model._meta.verbose_name.title()

    def ajax_handler(self, request):
        # This is an empty stub we can override in inheriting classes
        pass


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


class IngredientModalView(CreateUpdateMixin, ShortDescriptionMixin, JsonFormMixin, UpdateView):
    ''' Single class which handle the mixins using the modal edit form '''
    template_name = 'cocktails/modal_edit_form.html'

    def ajax_handler(self, request):
        ''' If the GET request has parameters corresponding to model properties,
        we will try to preload the form with the correct value
        '''
        self.object = self.get_object()
        form_class = self.get_form_class()

        if self.object is None:
            # Grab any valid initial values from the GET params
            initial = {}
            for key, value in request.GET.items():
                if hasattr(self.model, key):
                    initial[key] = value

            form = form_class(initial=initial)
        else:
            form = self.get_form(form_class)

        return self.render_to_response(self.get_context_data(form=form))


# ---------
# Home page
# ---------
class Home(TemplateView):
    template_name = 'cocktails/home.html'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            response = []

            model_type = request.GET.get('model')
            search_text = request.GET.get('search_text')

            model = apps.get_model('cocktails', model_type)
            query = model.objects.filter(name__contains=search_text)

            for item in query:
                D = item.to_dict()
                D['detail_url'] = item.get_absolute_url()
                response.append(D)

            return JsonResponse(response, safe=False)
        else:
            return super().get(request, *args, **kwargs)


# --------
# Cocktail
# --------
class CocktailDetail(JsonFormMixin, CreateUpdateMixin, UpdateView):
    model = Cocktail
    template_name = 'cocktails/cocktail_detail.html'
    form_class = CocktailForm


class CocktailCategoryEdit(IngredientModalView):
    model = CocktailCategory
    fields = ['name', 'description', 'image_url', 'wiki_url']


# ----------
# Ingredient
# ----------
class IngredientDetail(JsonFormMixin, CreateUpdateMixin, UpdateView):
    model = Ingredient
    template_name = 'cocktails/ingredient_detail.html'
    form_class = IngredientForm

    def ajax_handler(self, request):
        filter_class = request.GET.get('filter_class')
        filter_category = request.GET.get('filter_category')

        response = {}
        response['category_options'] = [{'value': '', 'text': '---------'}]
        response['subcategory_options'] = [{'value': '', 'text': '---------'}]

        if filter_class != '':
            cats = IngredientCategory.objects.filter(ingredient_class=filter_class).order_by('name')
            for cat in cats:
                response['category_options'].append({'value': cat.pk, 'text': cat.name})

        if filter_category != '':
            subcats = IngredientSubcategory.objects.filter(category=filter_category).order_by('name')
            for subcat in subcats:
                response['subcategory_options'].append({'value': subcat.pk, 'text': subcat.name})

        return JsonResponse(response, safe=False)


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


class IngredientClassEdit(IngredientModalView):
    model = IngredientClass
    fields = ['name', 'description', 'image_url', 'wiki_url']


class IngredientCategoryEdit(IngredientModalView):
    model = IngredientCategory
    fields = ['name', 'ingredient_class', 'description', 'image_url', 'wiki_url']


class IngredientSubcategoryEdit(IngredientModalView):
    model = IngredientSubcategory
    fields = ['name', 'category', 'description', 'image_url', 'wiki_url']


class BrandDetail(JsonFormMixin, CreateUpdateMixin, UpdateView):
    model = Brand
    template_name = 'cocktails/brand_detail.html'
    form_class = BrandForm


class DistilleryEdit(IngredientModalView):
    model = Distillery
    fields = ['name', 'description', 'country', 'us_state', 'city', 'image_url', 'wiki_url', 'own_url']


class ManufacturerEdit(IngredientModalView):
    model = Manufacturer
    fields = ['name', 'description', 'country', 'us_state', 'city', 'image_url', 'wiki_url', 'own_url']


# ---------------
# Class Instances
# ---------------
ingredient_detail = IngredientDetail.as_view()

ingredient_cat = IngredientCategorization.as_view()
ingredient_class_edit = IngredientClassEdit.as_view()
ingredient_category_edit = IngredientCategoryEdit.as_view()
ingredient_subcategory_edit = IngredientSubcategoryEdit.as_view()

brand_detail = BrandDetail.as_view()

distillery_edit = DistilleryEdit.as_view()
manufacturer_edit = ManufacturerEdit.as_view()

cocktail_detail = CocktailDetail.as_view()
cocktail_category_edit = CocktailCategoryEdit.as_view()
