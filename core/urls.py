from django.urls import path
from django.views.generic import TemplateView
from .views import HomeView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
]