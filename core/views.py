from django.shortcuts import render
from django.views import View
from core.models import Product

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
