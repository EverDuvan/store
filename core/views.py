from django.shortcuts import render
from django.views import View
from core.models import Product, ProductImage

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


def ProductView(request):
    products = Product.objects.all()
    # print(products)  # Añade esta línea para depurar
    return render(request, 'product.html', {'products': products})

def imageView(request):
    images = ProductImage.objects.all()
    return render(request, 'images.html', {'images': images})

