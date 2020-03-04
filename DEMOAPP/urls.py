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

urlpatterns = [
]
