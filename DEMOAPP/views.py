from flask import Flask, request, jsonify, make_response, render_template
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ProductForm
from .models import Product, BlogPage, BlogIndexPage, ContactUs
import webbrowser


def home(request):
    posts.Post.objects.all()
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')

    return render(request, 'base/home.html', {'posts': posts})


def confirm_email(request):

    subject = 'Thanks'
    message = 'For the nuts'
    from_email = settings.EMAIL_HOST_USER
    to_list = [settings.EMAIL_HOST_USER, 'joel08112@icloud.com']
    send_mail(subject, message, from_email, to_list, fail_silently=True)

    return render(request, 'confirm_email.html')


def email_verification(request):

    subject = 'Thanks'
    message = 'For the nuts'
    from_email = settings.EMAIL_HOST_USER
    to_list = [settings.EMAIL_HOST_USER, 'joel08112@icloud.com']
    send_mail(subject, message, from_email, to_list, fail_silently=True)

    return render(request, 'email_verification.html')


class RestrictedView(LoginRequiredMixin, TemplateView):
    template_name = ''
    raise_exception = True
    permission_denied_message = "You are not allowed here"




