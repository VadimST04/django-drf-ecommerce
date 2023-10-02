from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from product.models import Product, Brand, Category, ProductLine, ProductImage


class EditLinkInLine:
    def edit(self, instance):
        url = reverse(
            f'admin:{instance._meta.app_label}_{instance._meta.model_name}_change',
            args=[instance.pk]
        )
        if instance.pk:
            link = mark_safe(f'<a href="{url}">edit</a>')
            return link
        return ''


class ProductLineInLine(EditLinkInLine, admin.TabularInline):
    model = ProductLine
    readonly_fields = ['edit', ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInLine]


class ProductImageInLine(admin.TabularInline):
    model = ProductImage


@admin.register(ProductLine)
class ProductLineAdmin(admin.ModelAdmin):
    inlines = [ProductImageInLine]


admin.site.register(Brand)
admin.site.register(Category)
