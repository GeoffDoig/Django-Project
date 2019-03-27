from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

class OrderLineItemInline(admin.TabularInline):
    model = OrderLineItem
    
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderLineItemInline]
    
admin.site.register(Order, OrderAdmin)
