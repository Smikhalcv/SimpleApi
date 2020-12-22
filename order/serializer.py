from django.db import transaction
from rest_framework import serializers
from .models import Order, Product


class ProductOrderPositionSerializer(serializers.Serializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product.id'
    )
    name = serializers.CharField(
        source='product.name',
        read_only=True
    )
    quantity = serializers.IntegerField(
        min_value=1,
        max_value=10
    )


class OrderSerializer(serializers.ModelSerializer):
    positions = ProductOrderPositionSerializer(many=True)


    class Meta:
        model = Order
        fields = ('id', 'amount', 'comment', 'positions')

    def validate(self, attrs):
        print(attrs)

        return attrs

    @transaction.atomic
    def create(self, validated_data):
        print('Проверенно')
        return super().create(validated_data)