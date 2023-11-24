from django.urls import path
from . import views

urlpatterns = [


    path('', views.index, name="index"),
    path('base/', views.base, name="base"),
    # capturering details for system
    path('form/', views.form, name ="form"),
    path('patients/', views.patients, name="patients"),
    path('doctors/', views.doctors, name="doctors"),
    path('appointments/', views.appointments, name="appointments"),
    path('medical_records/', views. medical_records, name="medical_records"),
    path('departments/', views.departments, name="departments"),
    path('nurses/', views.nurses, name="nurses"),
    path('medications/', views.medications, name="medications"),
    path('tests/', views.tests, name="tests"),
    path('test_results/', views.test_results, name="test_results"),

    path('suppliers/', views.suppliers, name="suppliers"),

    path('purchase_orders/', views.purchase_orders, name="purchase_orders"),

    path('supplies/', views.supplies, name="supplies"),
    
    path('purchase_order_items/', views.purchase_order_items, name="purchase_order_items"),
    path('payments/', views.payments, name="payments"),
    path('invoices/', views.invoices, name="invoices"),
    path('employees/', views.employees, name="employees"),
    path('employee_attendance/', views.employee_attendance, name="employee_attendance"),
    path('tax_categories/', views.tax_categories, name="tax_categories"),
    path('invoice_tax/', views.invoice_tax, name="invoice_tax"),
    
    
    # path('departments/', views.departments, name=" departments"),
    # path('departments/', views.departments, name=" departments"),




]
