from rest_framework import serializers

from product.models import Category, Brand, Product, ProductLine, ProductImage, Attribute, AttributeValue


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', ]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ['id', 'productline', ]


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ['name', 'id', ]


class AttributeValueSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer()

    class Meta:
        model = AttributeValue
        fields = ['attribute', 'attribute_value', ]


class ProductLineSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many=True)
    attribute_value = AttributeValueSerializer(many=True)

    class Meta:
        model = ProductLine
        fields = [
            'price',
            'sku',
            'stock_qty',
            'order',
            'product_image',
            'attribute_value'
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        av_data = data.pop('attribute_value')
        attr_values = {}
        for key in av_data:
            attr_values.update({key['attribute']['id']: key['attribute_value']})
        data.update({'specifications': attr_values})
        return data


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name')
    category_name = serializers.CharField(source='category.name')
    product_line = ProductLineSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'
