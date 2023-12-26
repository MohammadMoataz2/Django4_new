from django.contrib import admin

# Register your models here.
from .models import *



class CustomersAdmin(admin.ModelAdmin):
    pass
    list_display = ["name", "phone" , "email" , "date_created"]
    list_display_links = ["name"]
    list_editable = [ "phone" , "email"]
    search_fields = ["name", "phone" , "email" , "date_created"]
    list_filter = ["name", "phone" , "email" , "date_created"]
    fields = ["name", "phone" , "email" ]

class TagsAdmin(admin.ModelAdmin):
    pass
    list_display = ["name"]
    list_display_links = ["name"]
    
    search_fields = ["name"]
    list_filter = ["name"]
   

class ProductsAdmin(admin.ModelAdmin):
    pass
    list_display = ["name", "price" , "category" , "date_created"]
    list_display_links = ["name"]
    list_editable = [ "price" , "category"]
    search_fields = ["name", "price" , "category" , "date_created" , "tags"]
    list_filter = ["name", "price" , "category" , "date_created" , "tags"]
    fields = ["name", "price" , "category"  , "tags"]





class OrdersAdmin(admin.ModelAdmin):
    pass
    list_display = ["customer", "product" , "date_created" , "status" , "note"]
    list_display_links = ["customer"]
    list_editable = [ "product" , "status" , "note"]
    search_fields = ["customer", "product" , "date_created" , "status" , "note"]
    list_filter = ["customer", "product" , "date_created" , "status" ,"note"]
    


admin.site.register(Customer,CustomersAdmin)
admin.site.register(Order,OrdersAdmin)
admin.site.register(Tag,TagsAdmin)
admin.site.register(Product,ProductsAdmin)