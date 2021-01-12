"""DEMOPROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls import include, url, handler404, handler500, handler403, handler400
from django.conf.urls.static import static
from django.views.generic import TemplateView
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
from allauth.account import *
from . import views
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
                  # path('admin/', admin.site.urls),
                  # path('', include('DEMOAPP.urls')),  # empty string because we want it to be mapped to the homepage
                  path('403/', TemplateView.as_view(template_name="DEMOAPP/403.html")),
                  path('404/', TemplateView.as_view(template_name="DEMOAPP/404.html")),
                  # path('architect-page/', views.view_architect_page),
                  # path('', views.view_home_page),
                  url('deleted/', views.delete_user, name='delete-user'),
                  url(r'^account/password/change/', views.password_redirect),
                  url(r'^account/', include('allauth.account.urls')),
                  url(r'^fun/', views.fun),
                  re_path(r'^admin/', include(wagtailadmin_urls)),
                  re_path(r'^documents/', include(wagtaildocs_urls)),
                  re_path(r'', include(wagtail_urls)),

                  # url(r��, include(wagtail_urls)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = TemplateView.as_view(template_name="DEMOAPP/404.html")
handler403 = TemplateView.as_view(template_name="DEMOAPP/403.html")

