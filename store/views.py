from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse_lazy

from store.models import *

# Create your views here.

# ---------------------------------------------------------------------------- #
#                                  store View                                  #
# ---------------------------------------------------------------------------- #

def store(request, category_slug=None):
    
    categories = None
    products = None
    
    if category_slug != None:
        try:
            categories = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.filter(category=categories, is_available=True)
        except:
            return redirect('store')
    else:
        products = Product.objects.all().filter(is_available=True)

    products_count = products.count()
    context = {'products' : products, 'products_count' : products_count, 'categories':categories}
    template_name = 'store/store.html'
    return render(request, template_name, context)



def product_detail(request, category_slug, product_slug):
    
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except :
        return redirect('products-by-category', category_slug)
    
    
    template_name = 'store/product_detail.html'
    context = {'single_product' : single_product}
    
    return render(request, template_name, context)


