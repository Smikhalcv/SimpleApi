from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from order.filters import OrderFilter
from order.models import Order
from order.serializer import OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = OrderFilter

    # @transaction.atomic
    # def create(self, request, *args, **kwargs):
    #     print('Создание внутри транзакции')
    #     return super().create(request, *args, **kwargs)