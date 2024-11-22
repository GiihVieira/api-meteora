from django.contrib import admin
from meteora.models import Product, Category


class Products(admin.ModelAdmin):
    list_display        = ('id', 'name', 'description', 'price', 'qtd_stock', 'category', 'image', 'make_in', 'update_in')
    list_display_links  = ('id', 'name',)
    list_per_page       = 10
    search_fields       = ('name', 'price',)
    ordering_fields     = ('name',)

admin.site.register(Product, Products)


class Categories(admin.ModelAdmin):
    list_display        = ('id', 'name', 'description', 'make_in', 'update_in')
    list_display_links  = ('id', 'name')
    search_fields       = ('name', )
    ordering_fields     = ('name', )

admin.site.register(Category, Categories)
