from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .decorators import allowed_users
from .forms import ProductForm, TypeForm
from .models import Product, BlogPage, BlogIndexPage, ContactUs, Type
import webbrowser
from .models import ProTec, ProTecGalleryImage


def home(request):
    posts.Post.objects.all()
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')

    return render(request, 'base/home.html', {'posts': posts})


class RestrictedView(LoginRequiredMixin, TemplateView):
    template_name = ''
    raise_exception = True
    permission_denied_message = "You are not allowed here"


def product_view(request, product_id):
    """View the product pages."""
    obj = Product.objects.get(id=product_id)
    colours = ProTecGalleryImage.objects.all()
    pro_tec = ProTec.objects.all()
    print(obj)
    print(obj.id)
    print(pro_tec)
    print(colours)

    context = {
        'obj': obj,
        'colours': colours,
        'pro_tec': pro_tec
    }
    return render(request, 'django_database/product.html', context)


def main_view(request):
    """View the all products."""
    products = Product.objects.all().order_by('id')
    security = Product.objects.filter(heading__name__in=['Security']).order_by('id')
    environment = Product.objects.filter(heading__name__in=['Environment']).order_by('id')
    architecture = Product.objects.filter(heading__name__in=['Architecture']).order_by('id')
    fire = Product.objects.filter(heading__name__in=['Fire']).order_by('id')

    context = {
        'products': products,
        'security': security,
        'environment': environment,
        'architecture': architecture,
        'fire': fire
    }
    return render(request, 'django_database/main.html', context)


def select_view(request, product_type):
    """View the all products in type."""
    item = Product.objects.filter(heading__name__in=[product_type]).order_by('id')

    print("new")

    context = {
        'item': item,
        'product_type': product_type
    }
    return render(request, 'django_database/list.html', context)


@login_required
@allowed_users(allowed_roles=['Moderators'])
def add_product(request):
    """Add a new product name."""
    form = ProductForm()
    products = Product.objects.all()

    context = {
        'form': form,
        'products': products
    }
    return render(request, 'django_database/add_product.html', context)


@require_POST
@login_required
@allowed_users(allowed_roles=['Moderators'])
def add_product_view(request):
    """Add to product pages."""
    form_id = ''
    if request.method == 'POST':
        print("Printing POST")
        form = ProductForm(request.POST, files=request.FILES,)
        if form.is_valid():
            print("Valid")
            form.save()
            return redirect('/site/product/add')
        else:
            print(form.errors)
            return redirect('/site/product/add')


@login_required
@allowed_users(allowed_roles=['Moderators'])
def update_product_view(request, product_id):
    """Edit existing product form view."""

    obj = Product.objects.get(pk=product_id)
    form = ProductForm(instance=obj)
    products = Product.objects.all()
    if request.method == 'POST':
        print("Printing POST")
        form = ProductForm(request.POST, files=request.FILES,  instance=obj)
        print(obj)
        if form.is_valid():
            print("Valid")
            print(str(obj.product_picture))
            form.save()
            return redirect('/site/product/'+product_id+'/update')
        else:
            print(form.errors)
            return redirect('/site/product/'+product_id+'/update')

    context = {
        'obj': obj,
        'form': form,
        'products': products
    }

    return render(request, 'django_database/update_product.html', context)


@login_required
@allowed_users(allowed_roles=['Moderators'])
def delete_product(request, product_id):
    Product.objects.get(pk=product_id).delete()
    return redirect('/site/product/add')


def type_view(request, type_id):
    """View the type pages."""
    obj = Type.objects.get(pk=type_id)

    context = {
        'obj': obj
    }
    return render(request, 'django_database/type.html', context)


@login_required
@allowed_users(allowed_roles=['Moderators'])
def add_type(request):
    """Add a new type name."""
    form = TypeForm()
    types = Type.objects.all()

    context = {
        'form': form,
        'types': types
    }
    return render(request, 'django_database/add_type.html', context)


@require_POST
@login_required
@allowed_users(allowed_roles=['Moderators'])
def add_type_view(request):
    """Add to type pages."""
    form_id = ''
    if request.method == 'POST':
        print("Printing POST")
        form = TypeForm(request.POST)
        if form.is_valid():
            print("Valid")
            form.save()
            return redirect('/site/type/add')
        else:
            print(form.errors)
            return redirect('/site/type/add')


@login_required
@allowed_users(allowed_roles=['Moderators'])
def update_type_view(request, type_id):
    """Edit existing type form view."""

    obj = Type.objects.get(pk=type_id)
    form = TypeForm(instance=obj)
    types = Type.objects.all()
    if request.method == 'POST':
        print("Printing POST")
        form = TypeForm(request.POST, instance=obj)
        print(obj)
        if form.is_valid():
            print("Valid")
            form.save()
            return redirect('/site/type/'+type_id+'/update')
        else:
            print(form.errors)
            return redirect('/site/type/'+type_id+'/update')

    context = {
        'obj': obj,
        'form': form,
        'types': types
    }

    return render(request, 'django_database/update_type.html', context)


@login_required
@allowed_users(allowed_roles=['Moderators'])
def delete_type(request, type_id):
    Type.objects.get(pk=type_id).delete()
    return redirect('/site/type/add')



