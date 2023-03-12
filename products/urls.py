from django.contrib import admin  
from django.urls import path  
from products import views
from . import views

urlpatterns = [
    
    path('products/',views.ProductListView.as_view(),name='product-list'),
    path('products/<int:pk>/',views.ProductDetailView.as_view(),name='product-detail'),
    path('category/',views.CategoryListView.as_view(),name='category-list'),
    path('category/<int:pk>/',views.CategoryDetailView.as_view(),name='category-detail'),
    path('products/<int:products_id>/files/',views.FileListView.as_view(),name='file-list'),
    path('products/<int:products_id>/files/<int:pk>/',views.FileDetailView.as_view(),name='file-detail'),

]
