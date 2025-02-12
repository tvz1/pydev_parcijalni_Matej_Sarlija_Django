from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),           # List all customers
    path('<int:pk>/', views.customer_detail, name='customer_detail'),  # View details of a single customer
    path('create/', views.customer_create, name='customer_create'),    # Create a new customer
    path('<int:pk>/update/', views.customer_update, name='customer_update'),  # Update an existing customer
]
