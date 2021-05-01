from django.urls import path
from . import views


# Adding URL that render page from views.py

urlpatterns = [
    path('', views.home),
    path('products/', views.products),
    path('customer/', views.customer),
]

