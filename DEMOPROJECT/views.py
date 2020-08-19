from django.contrib.auth.views import redirect_to_login
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
from django.urls import reverse
from django.contrib.auth import logout


def fun(request):
    return HttpResponse('fun')


def password_redirect(request):
    response = redirect('/account/password/reset')
    return response


def handler500(request, *args, **argv):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


class PasswordResetDoneView(TemplateView):
    template_name = (
        "404")


pg_404 = PasswordResetDoneView.as_view()


@login_required
def view_architect_page(request):
    args = {'user': request.user}
    return render(request, 'DEMOAPP/architect_page.html', args)


@login_required
def view_home_page(request):
    args = {'user': request.user}
    return render(request, 'DEMOAPP/home_page.html', args)


def redirect_to_my_auth(request):
    return redirect_to_login(reverse('wagtailadmin_home'), login_url='account/login')


def delete_user(request):
    request.user.delete()
    logout(request)
    return redirect('/')

