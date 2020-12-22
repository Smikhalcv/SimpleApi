from django_filters import rest_framework as filters
from .models import Order


class OrderFilter(filters.FilterSet):
    id = filters.ModelMultipleChoiceFilter(
        field_name='id',
        to_field_name='id',
        queryset=Order.objects.all()
    )
    amount_less = filters.NumberFilter(
        field_name='amount',
        lookup_expr='lte',
    )
    amount_greater = filters.NumberFilter(
        field_name='amount',
        lookup_expr='gte',
    )

    class Meta:
        model = Order
        fields = ('id', 'amount', )