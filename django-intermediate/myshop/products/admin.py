from django.contrib import admin
from .models import Shirt, Product


class ProductAdmin(admin.ModelAdmin):
    """Class for customizing the admin panel."""
    readonly_fields = ("slug",)
    list_display = ("title", "id", "category", "is_bestseller")
    list_filter = ("is_bestseller",)
    search_fields = ("title", "category", "brand")


# Register your models here.
admin.site.register(Shirt)
admin.site.register(Product, ProductAdmin)