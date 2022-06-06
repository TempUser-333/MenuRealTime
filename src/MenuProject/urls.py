"""MenuProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MenuApp.views import (InsertSampleData,
                           GetCategoriesInTheMenu,
                           CheckThePresenceOfMenuItemsInTheCategories,
                           GetMenuItemsInTheCategories,
                           CheckForSubCategoriesInTheCategories,
                           GetSubCategoriesInTheCategories,
                           CheckForMenuItemsInTheSubCategories,
                           GetMenuItemsInTheSubCategories,
                           GetOverviewOfTheEntireMenu,)
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert/entire/data/', InsertSampleData.as_view()),
    path('get/all/the/categories/in/the/menu/', GetCategoriesInTheMenu.as_view()),
    path('get/favicon/', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico/'))),
    path('check/for/the/presence/of/menuitems/in/the/categories/', CheckThePresenceOfMenuItemsInTheCategories.as_view()),
    path('get/menuitems/in/the/categories/', GetMenuItemsInTheCategories.as_view()),
    path('check/for/subcategories/in/the/categories/', CheckForSubCategoriesInTheCategories.as_view()),
    path('get/subcategories/in/the/categories/', GetSubCategoriesInTheCategories.as_view()),
    path('check/for/menuitems/in/the/subcategories/', CheckForMenuItemsInTheSubCategories.as_view()),
    path('get/menuitems/in/the/subcategories/', GetMenuItemsInTheSubCategories.as_view()),
    path('get/overview/of/the/entire/menu/', GetOverviewOfTheEntireMenu.as_view()),
]
