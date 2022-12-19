from django.urls import path
from . import views


app_name = 'product'
urlpatterns = [

    path('index/', views.product, name='index'),
    path('purchase/', views.purchase, name='purchase'),
    path('product_check/', views.product_check, name='product_check'),
    path('product_cancel/', views.product_cancel, name='product_cancel'),

    

    
]