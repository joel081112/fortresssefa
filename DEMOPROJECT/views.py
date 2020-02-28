from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class RestrictedView(LoginRequiredMixin, TemplateView):
    template_name = 'DEMOAPP/templates/DEMOAPP/architect_page.html'
    raise_exception = True
    permission_denied_message = "You are not allowed here"


def fun(request):
    return HttpResponse('fun')
