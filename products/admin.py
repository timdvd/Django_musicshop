from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title', 'category']
    list_display = ['title', 'category', 'author', 'price', 'discount_price', 'active', 'timestamp']
    list_editable = ['price', 'discount_price', 'active']
    list_filter = ['category', 'active', 'author']
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
