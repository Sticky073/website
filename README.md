## This Website

This is a personal website built using Django. It is currently acting as a learning tool for Django development, though I expect it to morph into a fully functioning database/blog in due time. 

## Cocktails

The main app on this site (for now) is a cocktail recipe database. I have been really into craft cocktails for the past two years, and have several books and favorite blogs. However, none of the recipes contained therein are sortable, searchable, etc. This app will allow me (or users in the future) to aggregate all these recipes and search by names, ingredient(s), type, and possibly tags. 

## Coding Methods

Currently, I am using vanilla Django on the backend and supporting the templates with Bootstrap and JQuery on the front end. I am slowly adding AJAX functionality to pages to make them more modern and get rid of page loads. 

Once the core site is done, I may switch over the the Django Rest Framework and a front-end framework, assuming things are still relatively simple and don't require a ton of refactoring. Even without DRF, I would like to start practicing with Angular 2 (or 4, which is out soon) once I've got Django under my belt. 

## Installation

I keep forgetting that `mysqlclient` has been failing to install using `pip` on Windows 10 64-bit, so I'm putting a note here. The solution is to install directly from a wheel, which I obtained at [Christopher Gohlke's site](http://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python).

Edit: I've just commited the wheel file for now and added it back into requirements.txt in order to preserve the correct version. I will work on finding a proper solution so the normal `pip install` works in the future.