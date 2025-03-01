from django.shortcuts import render, get_object_or_404
from .models import Product



def index_view(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'main/index.html', {'products': products})


def product_detail_view(request, product_id):
    product = get_object_or_404(Product,id=product_id)
    return render(request, 'main/product_detail.html', {'product': product})
