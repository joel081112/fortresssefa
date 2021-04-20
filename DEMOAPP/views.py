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


class RestrictedView(LoginRequiredMixin, TemplateView):
    template_name = ''
    raise_exception = True
    permission_denied_message = "You are not allowed here"




