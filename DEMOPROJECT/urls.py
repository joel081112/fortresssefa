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
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
from allauth.account import *
from . import views


urlpatterns = [
                  # path('admin/', admin.site.urls),
                  # path('', include('DEMOAPP.urls')),  # empty string because we want it to be mapped to the homepage

                  url(r'^yeet', views.handler404),
                  url(r'^account/password/change/', views.password_redirect),
                  url(r'^account/', include('allauth.account.urls')),
                  url(r'^fun/', views.fun),
                  re_path(r'^admin/', include(wagtailadmin_urls)),
                  re_path(r'^documents/', include(wagtaildocs_urls)),
                  re_path(r'', include(wagtail_urls)),

                  # url(r��, include(wagtail_urls)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'DEMOPROJECT.views.handler404'
handler500 = 'DEMOPROJECT.views.handler500'