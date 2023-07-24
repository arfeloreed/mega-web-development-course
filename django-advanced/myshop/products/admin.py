from django.contrib import admin
from .models import Product, Brand, Address, Category, Feedback


class ProductAdmin(admin.ModelAdmin):
    """Class for customizing the admin panel."""
    readonly_fields = ("slug",)
    list_display = ("title", "id", "is_bestseller")
    list_filter = ("is_bestseller",)
    search_fields = ("title", "category", "brand")


# Register your models here.
admin.site.register(Feedback)
admin.site.register(Category)
admin.site.register(Address)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)