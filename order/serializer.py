from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Order, Product, ProductOrderPosition


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
        positions = attrs.get('positions')
        if not positions:
            raise ValidationError({'positions': 'Не указан список товаров'})
        set_positions = set(position['product']["id"] for position in positions)
        if len(positions) != len(set_positions):
            raise ValidationError({'positions': 'Есть повторы продуктов'})
        return attrs

    @transaction.atomic
    def create(self, validated_data):
        print('Проверенно')
        positions = validated_data.pop('positions')
        order = super().create(validated_data)
        for position in positions:
            ProductOrderPosition.objects.create(
                product=position['product']['id'],
                order=order,
                quantity=position['quantity']
            )
        return order