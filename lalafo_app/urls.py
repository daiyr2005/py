
from django.urls import path

from .models import Product
from .views import CategoryListView, ProductListView, ProductDetailView

urlpatterns = [
    path('category/', CategoryListView.as_view(), name = 'category-list'),
    path('product/', ProductListView.as_view(), name= 'product-list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name= 'product-detail'),
]
