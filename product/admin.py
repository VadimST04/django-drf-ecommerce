from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from product.models import Product, Brand, Category, ProductLine, ProductImage, AttributeValue, Attribute, ProductType


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


class AttributeValueInLine(admin.TabularInline):
    model = AttributeValue.product_line_attribute_value.through


@admin.register(ProductLine)
class ProductLineAdmin(admin.ModelAdmin):
    inlines = [ProductImageInLine, AttributeValueInLine]


class AttributeInLine(admin.TabularInline):
    model = Attribute.product_type_attribute.through


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [AttributeInLine, ]


admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
