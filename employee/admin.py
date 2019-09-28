from django.contrib import admin
from .models import employees, products, ordered_lists

# Register your models here.
admin.site.register(employees)
admin.site.register(products)
admin.site.register(ordered_lists)
