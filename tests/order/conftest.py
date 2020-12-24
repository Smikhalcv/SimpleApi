import pytest
from model_bakery import baker

from order.models import Order


# @pytest.fixture
# def order_factory():
#     def factory(**kwargs):
#         params = {
#             'amount': 100
#         }
#         params.update(kwargs)
#         order = Order.objects.create(**params)
#         return order
#     return factory


@pytest.fixture
def order_factory():
    def _factory(**kwargs):
        order = baker.make('order.Order', **kwargs)
        return order
    return _factory