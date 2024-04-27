from django.contrib import admin
from ecomapp.models import Products

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
admin.site.register(Products,ProductAdmin)