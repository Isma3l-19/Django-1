from django.urls import path
from . import views

urlpatterns = [
    path('', views.geeks_view, name='geeks_view'),
    path('example/', views.example_view, name='example_view'),
]