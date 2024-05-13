from django.contrib import admin

# Register your models here.

from .models import *
from django.contrib.auth.models import User

admin.site.register(Product)
admin.site.register(Tags)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(BrandImage)
admin.site.register(ProductImage)
admin.site.register(Subcategory)
admin.site.register(CategoryImage)
admin.site.register(SubcategoryImage)

