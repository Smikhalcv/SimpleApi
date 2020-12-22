from rest_framework.routers import SimpleRouter
from .api_views import OrderViewSet


router = SimpleRouter()
router.register('orders', OrderViewSet, basename='orders')


urlpatterns = [

] + router.urls

