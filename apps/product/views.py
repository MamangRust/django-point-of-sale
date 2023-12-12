from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductForm
from .models import Product


class ProductListView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login/"

    def get(self, request):
        products = Product.objects.all()
        return render(request, "admin/product/index.html", {"products": products})


class ProductCreateView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login/"

    def get(self, request):
        form = ProductForm()
        return render(request, "admin/product/create.html", {"form": form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_list")
        return render(request, "create_product.html", {"form": form})


class ProductEditView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login/"

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        return render(request, "admin/product/edit.html", {"form": form})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_list")
        return render(request, "admin/product/edit.html", {"form": form})


class ProductDeleteView(LoginRequiredMixin, View):
    redirect_field_name = "/auth/login/"

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect("product_list")
