from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-customer/', views.add_customer, name='add_customer'),
    path('old-customers/', views.old_customers, name='old_customers'),
    path('customer/<int:id>/', views.customer_detail, name='customer_detail'),
    path('delete-customer/<int:id>/', views.delete_customer, name='delete_customer'),
    path('edit-customer/<int:id>/', views.edit_customer, name='edit_customer'),
]
