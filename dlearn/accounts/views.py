from django.shortcuts import render,redirect
from .models import *
from .forms import OrderForm,CustomerForm
# Create your views here.
from django.forms import inlineformset_factory #create multiple form in one form
from django.http import HttpResponse
from .filters import OrderFilter
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()

    context = {
        'orders':orders,
        'customers' : customers,
        'total_orders':total_orders,
        'delivered':delivered,
        'pending': pending,


    }
    return render(request,'accounts/dashboard.html',context)


 
def products(request):
    products = Product.objects.all()

    return render(request,'accounts/products.html' , {"products":products})



def customers(request,pk):

    customer = Customer.objects.get(id = pk)
    orders  = customer.order_set.all()
    
    order_count = orders.count()
    myFilter = OrderFilter(request.GET , queryset = orders)
    orders = myFilter.qs
    context = {
        'customer':customer,
        'orders' : orders,
        'order_count':order_count,
        'myFilter':myFilter
    }
    return render(request,'accounts/customers.html',context)


def createOrder(request):

    form = OrderForm()
    context = {'form':form}

    if request.method == 'POST':
        #print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'accounts/order_form.html',context)


def createCustomer(request):

    form = CustomerForm()
    context = {'form':form}

    if request.method == 'POST':
        #print(request.POST)
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'accounts/customer_form.html',context)

def updateOrder(request,pk):
    order = Order.objects.get(id = pk)
    form = OrderForm(instance = order)

    
    if request.method == 'POST':
        #print(request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
        

    context = {'form':form}
    return render(request,'accounts/order_form.html',context)

def deleteOrder(request,pk):
    order = Order.objects.get(id = pk)

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {
        'item':order,
    }
    return render(request, 'accounts/delete.html', context)




def createOrderCustomer(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order , fields = ('product','status') , extra = 10) #parent and children
    customer = Customer.objects.get(id = pk)

    # form = OrderForm(initial = {
    #     'customer':customer,

    # })

    formset = OrderFormSet(queryset=Order.objects.none(),instance = customer)
    context = {
     #   'form':form,
        'formset' : formset}
    
    formset = OrderFormSet(request.POST,instance = customer)

    if request.method == 'POST':
        #print(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    return render(request,'accounts/ordercustomer_form.html',context)
