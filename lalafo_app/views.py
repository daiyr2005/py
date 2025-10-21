from django.views.generic import ListView, DetailView
from .models import Category, Product

class CategoryListView(ListView):
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'category.html'


class ProductListView(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'products_list.html'


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    context_object_name = 'products_detail'
    template_name = 'product_detail.html'


# Create your views here.
