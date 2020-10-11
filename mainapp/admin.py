from django.contrib import admin
from .models import categories, products, query, product_pictures
# Register your models here.

admin.site.register(categories)
admin.site.register(products)
admin.site.register(query)
admin.site.register(product_pictures)