from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','images','descriptions')
    
admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Cart)
