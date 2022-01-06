from django.http import HttpResponse
from django.shortcuts import render, redirect

from store.models import *



# ---------------------------------------------------------------------------- #
#                                  index View                                  #
# ---------------------------------------------------------------------------- #

def index(request):
    
    products = Product.objects.all().filter(is_available=True)
    
    context = {'products' : products}
    template_name = 'index.html'
    
    return render(request, template_name, context)


