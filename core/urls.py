from django.urls import path
from django.views.generic import TemplateView
from .views import HomeView, ProductView, imageView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('product/', ProductView, name='products'),
    path('image/', imageView, name='image_list'),
    
]