from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cocktail_home, name='cocktail_home'),
    url(r'^ingredient/(?P<pk>\d+)/$', views.ingredient_detail, name='ingredient_detial')
]