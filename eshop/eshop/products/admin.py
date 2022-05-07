from django.contrib import admin

from eshop.products.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('product_type', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'available', 'created', )
    list_filter = ('available', 'created', 'updated', )
    list_editable = ('product_price', 'available', )

