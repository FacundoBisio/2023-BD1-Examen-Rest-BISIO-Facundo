from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Customers, Suppliers, Categories, Products, Orders, Orderdetails, Employees

class SerializadorPadre(ModelSerializer):
    class Meta:
        fields = '__all__'

class CustomerSerializer(SerializadorPadre):
    class Meta:
        model = Customers
        fields = '__all__'

class SupplierSerializer(SerializadorPadre):
    class Meta:
        model = Suppliers
        fields = '__all__'

class EmployeeSerializer (SerializadorPadre):
   class Meta:
      model = Employees
      fields = '__all__'

class CategorieSerializer (SerializadorPadre):
   class Meta:
      model = Categories
      fields = '__all__'

class ProductSerializer (SerializadorPadre):
   categoryid = CategorieSerializer(many=False, required=False)

   class Meta:
      model = Products
      fields = '__all__'

class OrderSerializer(SerializadorPadre):
   employeeid = EmployeeSerializer(many=False, required=False)
   class Meta:
      model = Orders
      fields = '__all__'

class OrderdetailSerializer (SerializadorPadre):
   class Meta:
      model = Orderdetails
      fields = '__all__'

class EstructuraSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=5)
    nombre = serializers.CharField(max_length=50)
    nombre_compañia = serializers.CharField(max_length=50)
    telefono = serializers.CharField(max_length=20)

class TodoSerializer (SerializadorPadre):
   orderid = OrderSerializer(many=False, required=False)
   productid = ProductSerializer(many=False, required=False)

   id = serializers.IntegerField()
   nombre = serializers.CharField()
   category = serializers.IntegerField()


class Punto1Serializer(serializers.Serializer):
   id = serializers.IntegerField()
   nombre = serializers.CharField()
   GananciaTotales = serializers.IntegerField()
   HireDate = serializers.DateTimeField()


class Filtro4Serializer(serializers.Serializer):
   id = serializers.IntegerField()
   apellido = serializers.CharField()
   nombre = serializers.CharField()
   birthdate = serializers.DateTimeField()
   country = serializers.CharField()
   newCountry = serializers.CharField()