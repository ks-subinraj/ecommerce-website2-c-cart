from django.contrib import admin
from .models import Category, Product
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug',]
    prepopulated_fields = {'slug':('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['price','stock','available']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)