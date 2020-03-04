from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, render_to_response
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import UpdateView
from django.http import Http404
from django.template import RequestContext


def fun(request):
    return HttpResponse('fun')


def password_redirect(request):
    response = redirect('/account/password/reset')
    return response


def handler404(request, exception, template_name="not_found.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
