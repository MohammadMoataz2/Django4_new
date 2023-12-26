from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length = 50 , null = True)
    phone = models.CharField(max_length = 50, null = True)
    email = models.CharField(max_length = 50, null = True)
    date_created = models.DateField(auto_now_add = True, null = True)
    
    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length = 50 , null = True)

    def __str__(self):
        return self.name
    

class Product(models.Model):

    CATEGORY = [

        ('Indoor',"Indoor"),
        ('Out Door',"Out Door")

    ]


    name = models.CharField(max_length = 50 , null = True)
    price = models.FloatField( null = True)
    category = models.CharField(max_length = 50 , null = True , choices = CATEGORY)
    describtion = models.TextField(max_length = 200 , null = True)
    date_created = models.DateField(auto_now_add = True, null = True)

    tags = models.ManyToManyField(Tag)

    
    
    def __str__(self):
        return self.name



class Order(models.Model):
    customer =models.ForeignKey(Customer,null = True , on_delete = models.SET_NULL)

    product = models.ForeignKey(Product,null = True , on_delete = models.SET_NULL)

    STATUS = [

            ("Pending", 'Pending'),
            ('Out for delivery' , 'Out for delivery'),
            ('Delivered','Delivered')



    ]
    date_created = models.DateField(auto_now_add = True, null = True)
    status = models.CharField(max_length = 50 , null = True , choices = STATUS)
    note = models.CharField(max_length = 50 , null = True)

    def __str__(self):
        return self.product.name

# class ParentModel(models.Model):
#     name = models.CharField(max_length = 200, null =True)

# class ChildModel(models.Model):
#     parent = models.ForeignKey(ParentModel)
#     name = models.CharField(max_length = 200, null = True)

# parent = ParentModel.objects.first()

# parent.childmodel_set.all()
    
# python manage.py shell
# from accounts.models import *
# customers = Customer.objects.all()
# print(customers) 
# print(customers.first()) 
# >>> customer1 = Customer.objects.get(name = "Mohammad") 
# >>> print(customer1.email) 
# >>> print(customer1.id)    
# 1
# >>> orders = customer1.order_set.all()
# >>> print(orders) 
# <QuerySet [<Order: Order object (1)>]>
# >>> print(orders[0]) 
# Order object (1)
# >>> order = Order.objects.first()
# >>> print(order.customer.name) 
# Mohammad
    
# >>> products = Product.objects.filter()
# >>> print(products)
# <QuerySet [<Product: Basketball>]>
# >>> products = Product.objects.filter(category = "Out Door") 
# >>> print(products) 
# <QuerySet []>
# >>> products = Product.objects.filter(category = "Out Door" , name = "") 
# >>> products = Product.objects.all().order_by('id')         
# >>> print(products) 
# <QuerySet [<Product: Basketball>]>   


# >>> products = Product.objects.filter(tags__name = "sports")             
# >>> print(products) 
# <QuerySet []>


# ballOrders = firstCustomer.order_set.filter(product__name = "Ball").count()

# # return total count for each product ordered
# allOrders = {}

# for order in firstCustomer.order_set.all():
#     if order.product.name in allOrders:
#         allOrders[order.product.name] +=1
#     else:
#         allOrders[order.product.name] = 1

# return allOrders : {'Ball : 2 , 'BBQ Grill' : 1}