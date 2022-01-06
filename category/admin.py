from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from category.models import *

# Register your models here.
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('category_name', )}  # Tuple within dictionary will make slug filed auto pupulated same as category_name
    list_display = ('category_name', 'slug')
    

admin.site.register(Category, CategoryAdmin)