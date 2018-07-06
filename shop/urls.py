from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.product_list, name='product_list'),
    path('shop/<str:category_slug>/', views.product_list, name='product_list_by_category'),
    path('shop/<str:slug>', views.product_detail, name='product_detail'),
]
