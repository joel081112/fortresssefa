from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
from allauth.account import *
from . import views
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    # page needs fixed

    path('main', views.main_view, name='main'),
    path('<product_type>', views.select_view, name='selector'),

    path('view_product/<product_id>', views.product_view, name='viewproduct'),
    path('product/<product_id>/update', views.update_product_view, name='update_product'),
    path('product/add', views.add_product, name='add_product'),
    path('product/add/new', views.add_product_view, name='add_new_product'),
    path('product/<product_id>/delete', views.delete_product, name='delete_product'),

    path('type/<type_id>', views.type_view, name='viewtype'),
    path('type/<type_id>/update', views.update_type_view, name='update_type'),
    path('type/add', views.add_type, name='add_type'),
    path('type/add/new', views.add_type_view, name='add_new_type'),
    path('type/<type_id>/delete', views.delete_type, name='delete_type'),

]
