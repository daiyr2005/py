
from django.urls import path

from .models import Product
from .views import (CategoryListView, ProductListView,
                    ProductDetailView, ProductCreateView,ProductUpdateView,ProductDeleteView)

urlpatterns = [
    path('category/', CategoryListView.as_view(), name = 'category-list'),
    path('product/', ProductListView.as_view(), name= 'product-list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name= 'product_detail'),
    path('product_create/', ProductCreateView.as_view(), name = 'product_create'),
    path('product_update/<int:pk>/',ProductUpdateView.as_view(),name = 'product_update'),
    path('product_delete/<int:pk>/',ProductDeleteView.as_view(),name = 'product_delete')
]
