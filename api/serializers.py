from rest_framework import serializers
from .models import Customers, Suppliers, Categories, Products, Orders, Orderdetails, Employees

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = '__all__'

class CategorieSerializer (serializers.ModelSerializer):
   class Meta:
      model = Categories
      fields = '__all__'

class ProductSerializer (serializers.ModelSerializer):
   class Meta:
      model = Products
      fields = '__all__'

class OrderSerializer (serializers.ModelSerializer):
   class Meta:
      model = Orders
      fields = '__all__'

class OrderdetailSerializer (serializers.ModelSerializer):
   class Meta:
      model = Orderdetails
      fields = '__all__'

class EmployeeSerializer (serializers.ModelSerializer):
   class Meta:
      model = Employees
      fields = '__all__'


#class Punto1Serializer(serializers.Serializer):
#    id = serializers.IntegerField()
#    apellido = serializers.CharField(max_length=50)
#    descripcion = CondicionIvaSerializer(many=False)
#    telefono = serializers.IntegerField()
#    nuevoTelefono = serializers.IntegerField()