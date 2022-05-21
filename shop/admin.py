from django.contrib import admin

from django.conf import settings
from .models import *


class CharacteristicInline(admin.TabularInline):
    model = Characteristic
    raw_id_fields = ['product']


class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    raw_id_fields = ['product']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'stock', 'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated')
    list_editable = ('price', 'stock', 'available')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')
    inlines = (ProductImagesInline, CharacteristicInline)

    if not settings.DEBUG:
        def view_on_site(self, obj):
            url = reverse('product_detail', args=[obj.slug])
            return 'http://34.118.100.219' + url


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
