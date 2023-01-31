from django.contrib import admin

from .models import *

admin.site.register(ProductCategory)
admin.site.register(ProductTypes)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category', 'type')
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category', 'type')
    search_fields = ('name',)
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity')
    extra = 0


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create')
    fields = ('title', 'content', 'is_published', 'image')
    search_fields = ('title',)
