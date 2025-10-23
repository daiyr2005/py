from django.views.generic import (ListView, DetailView,
                                  CreateView,UpdateView,DeleteView)
from .models import Category, Product
from .forms import ProductForm
from django.urls import reverse_lazy

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


class ProductCreateView(CreateView):
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('product-list')

class ProductUpdateView(UpdateView):
    queryset = Product.objects.all()
    form_class = ProductForm
    template_name = 'product_update.html'
    success_url = reverse_lazy('product-list')

class ProductDeleteView(DeleteView):
    queryset = Product.objects.all()
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product-list')





# Create your views here.
