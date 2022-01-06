from category.models import *


# ---------------------------------------------------------------------------- #
#                               category_renderer                              #
# ---------------------------------------------------------------------------- #

def category_renderer(request):
    
    all_categories = Category.objects.all()
    
    context = {'all_categories' : all_categories}
    return context