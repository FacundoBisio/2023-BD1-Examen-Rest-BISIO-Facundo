from django.urls import path, include
from .views import *

urlpatterns = [
    path("customer/", getAllCustomers, name="getAllCustomers"),
    path("customer/<str:pk>", getCustomerById , name="getCustomerById"),

    path("supplier/", getAllSuppliers, name="getAllSuppliers"),
    path("supplier/<str:pk>", getSupplierById , name="getSupplierById"),

    path("category/", getAllCategories, name="getAllCategories"),
    path("category/<str:pk>", getCategoryById , name="getCategoryById"), 

    path("product/", getAllProducts, name="getAllProducts"),
    path("product/<str:pk>", getProductById , name="getProductById"), 

    path("order/", getAllOrders, name="getAllOrders"),
    path("order/<str:pk>/", getOrderById, name="getOrderById"),

    path("orderdetail/", getAllOrderDetails, name="getAllOrderDetails"),
    path("orderdetail/<str:pk>/<str:pk2>", getOrderDetailById, name="getOrderDetailById"),


    path("employee/", getAllEmployees, name="getAllEmployees"),
    path("employee/<str:pk>/", getEmployeeById, name="getEmployeeById"),

    #pruebas
    path('estructura/', getEstructura),
    path('fecha/', getOrderByDate),
    path('punto1/', probandoPunto1),
    path('filtro3/', probandoFiltro3),
    path('update/', updateFiltro),

    #examen
    path('prueba1/', getEmployees)
]