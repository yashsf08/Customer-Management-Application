from django.urls import path
from . import views


# Adding URL that render page from views.py

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>', views.customer, name="customer"),
]
