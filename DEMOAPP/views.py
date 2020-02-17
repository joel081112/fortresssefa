from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    posts.Post.objects.all()
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')

    return render(request, 'base/home.html', {'posts': posts})


def confirm_email(request):

    subject = 'Thanks'
    message = 'For the nuts'
    from_email = settings.EMAIL_HOST_USER
    to_list = [settings.EMAIL_HOST_USER, 'joelferguson98@gmail.com', 'jshaw@fortress-sefa.com']
    send_mail(subject, message, from_email, to_list, fail_silently=True)

    return render(request, 'confirm_email.html')


def email_verification(request):

    subject = 'Thanks'
    message = 'For the nuts'
    from_email = settings.EMAIL_HOST_USER
    to_list = [settings.EMAIL_HOST_USER, 'joelferguson98@gmail.com', 'jshaw@fortress-sefa.com']
    send_mail(subject, message, from_email, to_list, fail_silently=True)

    return render(request, 'email_verification.html')

