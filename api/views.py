from django.utils import timezone
from datetime import datetime
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from .models import Customers, Suppliers, Categories, Products, Orders, Orderdetails, Employees
from django.db.models import Q

@api_view(['GET'])
def getRoutes(request):
    routes = [{'Endpoint':'/customer',
               'method':'GET',
               'body':None,
               'description':'Regresa todos los customer'
               },
               {'Endpoint':'/customer',
               'method':'POST',
               'body':{
                   "customerid":"AAAAA",
                   "companyname":"nombre compañia"
               },
               'description':'Genera un nuevo customer'
               }]
    return Response(routes)

# --- COSTUMERS ------------------------------------------------------------------------------------
@api_view(["GET", "POST"])
def getAllCustomers(request):
    if request.method == "GET":
        customers = Customers.objects.all()
        #customers = Customers.objects.filter(contactname__startswith = 'M').order_by('contacttitle')[:3]
        #customers = Customers.objects.filter(contacttitle = 'Owner')[3:6]
        customersSerializers = CustomerSerializer(customers, many=True)
        return Response(customersSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        customerNuevo = CustomerSerializer(data = request.data)
        if customerNuevo.is_valid():
            customerNuevo.save()
            return Response(customerNuevo.data, status=status.HTTP_201_CREAT)
        return Response(customerNuevo.errors ,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def getCustomerById(request, pk):
    try:
        customer = Customers.objects.get(customerid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':

        request.data['customerid'] = pk
        if 'companyname' not in request.data:
            request.data['companyname'] = customer.companyname

        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_200_OK)

# --- SUPPLIERS ------------------------------------------------------------------------------------
@api_view(["GET", "POST"])
def getAllSuppliers(request):
    if request.method == "GET":         
        suppliers = Suppliers.objects.all()
        suppliersSerializers = SupplierSerializer(suppliers, many=True)
        return Response(suppliersSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        supplierNuevo = SupplierSerializer(data = request.data)
        if supplierNuevo.is_valid():
            supplierNuevo.save()
            return Response(supplierNuevo.data, status=status.HTTP_200_OK)
        return Response(supplierNuevo.errors ,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def getSupplierById(request, pk):
    try:
        supplier = Suppliers.objects.get(supplierid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        request.data['supplierid'] = pk
    
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        supplier.delete()
        return Response(status=status.HTTP_200_OK)

# --- CATEGORIES ------------------------------------------------------------------------------------
@api_view(["GET", "POST"])
def getAllCategories(request):
    if request.method == "GET":         
        categories = Categories.objects.all()
        categoriesSerializers = CategorieSerializer(categories, many=True)
        return Response(categoriesSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        categorieNuevo = CategorieSerializer(data = request.data)
        if categorieNuevo.is_valid():
            categorieNuevo.save()
            return Response(categorieNuevo.data, status=status.HTTP_200_OK)
        return Response(categorieNuevo.errors ,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def getCategoryById(request, pk):
    try:
        categorie = Categories.objects.get(categoryid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = CategorieSerializer(supplier)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        request.data['categoryid'] = pk
    
        serializer = CategorieSerializer(categorie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        categorie.delete()
        return Response(status=status.HTTP_200_OK)

# --- PRODUCTS ------------------------------------------------------------------------------------
@api_view(["GET", "POST"])
def getAllProducts(request):
    if request.method == "GET":
        products = Products.objects.all()         
        #products = Products.objects.filter(categoryid__categoryname__startswith = 'C')   
        #products = Products.objects.filter(supplierid__companyname__startswith = 'F')[:2]
        productSerializers = ProductSerializer(products, many=True)
        return Response(productSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        productNuevo = ProductSerializer(data=request.data)
        if productNuevo.is_valid():
            productNuevo.save()
            return Response(productNuevo.data, status=status.HTTP_200_OK)
        return Response(productNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def getProductById(request, pk):
    try:
        product = Products.objects.get(productid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['productid'] = pk
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_200_OK)

# --- ORDERS ------------------------------------------------------------------------------------

@api_view(["GET", "POST"])
def getAllOrders(request):
    if request.method == "GET":         
        orders = Orders.objects.all()
        orderSerializers = OrderSerializer(orders, many=True)
        return Response(orderSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        orderNuevo = OrderSerializer(data=request.data)
        if orderNuevo.is_valid():
            orderNuevo.save()
            return Response(orderNuevo.data, status=status.HTTP_200_OK)
        return Response(orderNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def getOrderById(request, pk):
    try:
        order = Orders.objects.get(orderid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['orderid'] = pk
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_200_OK)

# --- ORDER_DETAILS ------------------------------------------------------------------------------------

@api_view(["GET", "POST"])
def getAllOrderDetails(request):
    if request.method == "GET":         
        order_details = Orderdetails.objects.all()
        orderDetailsSerializers = OrderdetailSerializer(order_details, many=True)
        return Response(orderDetailsSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        orderDetailNuevo = OrderdetailSerializer(data=request.data)
        if orderDetailNuevo.is_valid():
            orderDetailNuevo.save()
            return Response(orderDetailNuevo.data, status=status.HTTP_200_OK)
        return Response(orderDetailNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def getOrderDetailById(request, pk, pk2):
    try:
        order_detail = Orderdetails.objects.get(orderid=pk, productid=pk2)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = OrderdetailSerializer(order_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['orderid'] = pk
        serializer = OrderdetailSerializer(order_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        order_detail.delete()
        return Response(status=status.HTTP_200_OK)

# --- EMPLOYEES ------------------------------------------------------------------------------------

@api_view(["GET", "POST"])
def getAllEmployees(request):
    if request.method == "GET":         
        employees = Employees.objects.all()
        employeeSerializers = EmployeeSerializer(employees, many=True)
        return Response(employeeSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        employeeNuevo = EmployeeSerializer(data=request.data)
        if employeeNuevo.is_valid():
            employeeNuevo.save()
            return Response(employeeNuevo.data, status=status.HTTP_200_OK)
        return Response(employeeNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def getEmployeeById(request, pk):
    try:
        employee = Employees.objects.get(employeeid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['employeeid'] = pk
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_200_OK)

# ---------------------------------------- PRUEBAS -------------------------------------------
#ESTRUCTURAS
@api_view(['GET'])
def getEstructura(request):
    customers = Customers.objects.filter(contactname__startswith = 'C')
    estructura = {"id":0,
                "nombre":None,
                "nombre compañia":None,
                "telefono":None}
    resultados =[ ]
    for customer in customers:
        resultado = {
            "id": customer.customerid,
            "nombre": customer.contactname,
            "nombre_compañia": customer.companyname,
            "telefono": customer.phone}
        resultados.append(resultado)
    
    serializado = EstructuraSerializer(resultados,many = True)
    return Response(serializado.data,status=status.HTTP_200_OK)

#FECHA RANGOS
@api_view(['GET'])
def getOrderByDate(request):
    start_date_str = request.GET.get('start_date', '1998-01-01')
    end_date_str = request.GET.get('end_date', '2100-12-31')

    # Convierte las cadenas de fecha a objetos de fecha
    start_date = timezone.make_aware(datetime.strptime(start_date_str, "%Y-%m-%d"))
    end_date = timezone.make_aware(datetime.strptime(end_date_str, "%Y-%m-%d"))

    orders = Orders.objects.filter(orderdate__range=[start_date, end_date])
    serializados = OrderSerializer(orders, many=True)
    return Response(serializados.data, status=status.HTTP_200_OK)

#
@api_view(['GET'])
def probandoPunto1(request):
    letra = request.query_params.get("letter")
    year = request.query_params.get("year")

    empleadosFiltrados = Employees.objects.filter(firstname__icontains = letra)
    resultados = []
    for e in empleadosFiltrados:
        resultado = {
            "id" : e.employeeid,
            "nombre" : e.firstname,
            "apellido" : e.lastname,
            "birthdate" : e.birthdate
        }
        if e.birthdate.year >= int(year):
            resultados.append(resultado)
    serializados = Punto1Serializer(resultados, many=True)
    return Response(serializados.data)

@api_view(["GET", 'UPDATE'])
def probandoFiltro3(request):

    employees = Employees.objects.filter(Q(country__icontains='a') | Q(country__icontains='e') | Q(country__icontains='i') | Q(country__icontains='o') | Q(country__icontains='u'), salary__gt=2800, birthdate__lt=datetime(1990, 1, 1))
    employees.update(salary=3000)
    # 2954.55
    # 3119.15

    employeeSerializers = EmployeeSerializer(employees, many=True)
    return Response(employeeSerializers.data, status=status.HTTP_200_OK)


@api_view(["GET", 'UPDATE'])
def updateFiltro(request):
    letra = request.query_params.get("letter")
    year = request.query_params.get("year")

    empleadosFiltrados = Employees.objects.filter(firstname__icontains = letra)
    resultados = []
    for e in empleadosFiltrados:
        resultado = {
            "id" : e.employeeid,
            "nombre" : e.firstname,
            "apellido" : e.lastname,
            "birthdate" : e.birthdate,
            "country" : e.country,
            "newCountry" : request.query_params.get("newCountry"),
        }
        if e.birthdate.year >= int(year):
            resultados.append(resultado)
            e.country = request.query_params.get("newCountry")
            e.save()

    serializados = Filtro4Serializer(resultados, many=True)
    return Response(serializados.data)

# Obtener todos los Empleados dados una Categoría (Categories.CategoryID) y una cantidad esperada de ganancias.
@api_view(["GET"])
def getEmployees(request):
    category_id = request.GET.get('categoryid')
    ventas_min = request.GET.get('ventasmin')

    try:
        
        category = YourCategoryModel.objects.get(CategoryID=category_id)
    except YourCategoryModel.DoesNotExist:
        return JsonResponse({"error": "Categoría no encontrada"}, status=404)

    
    end_date = datetime.now().replace(day=1) - timedelta(days=1)
    start_date = end_date - timedelta(days=90)

    
    Employees = Employees.objects.filter(
        orders__orderdetails__product__category=category,
        orders__orderdetails__unitprice__gt=0,
        orders__orderdetails__quantity__gt=0,
        orders__orderdate__range=[start_date, end_date]
    ).annotate(ganancias_totales=Sum('orders__orderdetails__unitprice' * 'orders__orderdetails__quantity'))

    Employees = Employees.filter(ganancias_totales__gt=ventas_min)

    if Employees.exists():
        
        Employees = Employees.order_by('-ganancias_totales')

        
        response_data = [
            {
                "EmployeeID": employee.EmployeeID,
                "NombreCompleto": employee.full_name(),
                "GananciasTotales": employee.ganancias_totales,
                "HireDate": employee.hiredate
            }
            for employee in employees
        ]

        return JsonResponse(response_data, status=200)
    else:
        return JsonResponse({}, status=204)



@api_view(["POST", "PUT"])
def update_products(request):
    fecha_inicio = request.POST.get('fechaInicio')
    category_id = request.POST.get('CategoryID')
    ventas_requeridas = request.POST.get('ventasRequeridas')
    aumento = request.POST.get('aumento')
    shipper_id = request.POST.get('ShipperID')

    try:
        category = Category.objects.get(CategoryID=category_id)
        shipper = Shipper.objects.get(ShipperID=shipper_id)
    except (Category.DoesNotExist, Shipper.DoesNotExist):
        return JsonResponse({"error": "Categoría o Shipper no encontrados"}, status=404)

    
    products = Product.objects.filter(
        category=category,
        orderdetails__order__orderdate__range=[fecha_inicio, datetime.now()],
    ).annotate(ventas_totales=Sum('orderdetails__unitprice' * 'orderdetails__quantity'))

    products = products.filter(ventas_totales__gt=ventas_requeridas)

    if products.exists():
        for product in products:
          
            product.unitprice += product.unitprice * aumento
            if product.ventas_totales == 2 * ventas_requeridas:
                product.unitprice += product.unitprice * aumento * 2
            elif product.ventas_totales < ventas_requeridas / 2:
                product.discontinued = 1

            
            if shipper.name.startswith('United'):
                product.ganancia = product.unitprice * product.ventas_totales * 0.8


            product.save()

        response_data = [
            {
                "ProductID": product.ProductID,
                "Category": {
                    "CategoryID": product.category.CategoryID,
                    "CategoryName": product.category.CategoryName,
                  
                },
                
                "PreviousPrice": product.unitprice / (1 + aumento),
                "PercentageIncrease": aumento * 100,
            }
            for product in products
        ]

        return Response(response_data, status=200)
    else:
        return Response({}, status=204)


#clientes = Clientes.objects.all()[:4]
#clientes = Clientes.objects.all().order_by('nombre', 'altura')
#clientes = Clientes.objects.all()
#clientes = Clientes.objects.filter(apellido='ALONSO')
#clientes = Clientes.objects.filter(cod_cliente__gte=5) <=#clientes = Clientes.objects.filter(cod_cliente__gte=5) <=
#clientes = Clientes.objects.filter(cod_cliente__lt=10) >
#clientes = Clientes.objects.filter(apellido__startswith = 'A')
#clientes = Clientes.objects.filter(nombre__startswith = 'A', cod_condicion_iva__gte=2 )
#serializados = ClientesSerializer(clientes,many = True)
#return Response(serializados.data)