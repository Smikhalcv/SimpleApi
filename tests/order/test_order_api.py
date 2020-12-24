from decimal import Decimal

import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIClient

from order.models import Order


@pytest.mark.django_db
def test_orders_list(api_client, order_factory):
    order = order_factory()

    url = reverse("orders-list")


    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert len(resp_json) == 1

    resp_order = resp_json[0]
    assert resp_order['id'] == order.id


@pytest.mark.django_db
def test_orders_get(api_client, order_factory):
    order = order_factory()

    url = reverse("orders-detail", args=[order.id,])

    resp = api_client.get(url)
    assert resp.status_code == HTTP_200_OK
    resp_json = resp.json()
    assert resp_json['id'] == order.id
    assert Decimal(resp_json['amount']) == Decimal(order.amount)
    assert resp_json['comment'] == order.comment
