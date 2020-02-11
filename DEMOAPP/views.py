from django.shortcuts import render

from django.core.paginator import Paginator


def home(request):
    posts.Post.objects.all()
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    return render(request, 'base/home.html', {'posts': posts})


def index(request):
    return render(request, 'confirm_email.html')
