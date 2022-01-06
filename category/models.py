from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)                  # unique category url
    description = models.TextField(max_length=300, blank=True )
    cat_image = models.ImageField(upload_to='photos/category', blank=True)
    
    class Meta:
        verbose_name = ('category')
        verbose_name_plural = ('categories')           # will change correct the model in django admin page
    
    def __str__(self):
        return self.category_name
    
    def get_absolute_url(self):
        return reverse('products-by-category', args=([self.slug]))
        # if category is selected on 'store' page then it will return back to 'products_by_category' url
        # which takes 'slug' as an argument