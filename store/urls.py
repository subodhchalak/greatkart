from django.urls import path

from store.views import *

urlpatterns = [
    path('', store, name='store'),
    path('<slug:category_slug>/', store, name='products-by-category'),
    path('<slug:category_slug>/<slug:product_slug>/', product_detail, name='product-detail' )
]