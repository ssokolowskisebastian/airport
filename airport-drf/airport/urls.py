from rest_framework import routers
from .views import (
    AirportViewSet,
    RouteViewSet,
    AirplaneTypeViewSet,
    AirplaneViewSet,
    FlightViewSet,
    CrewViewSet,
    OrderViewSet,
    TicketViewSet
)
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'airports', AirportViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'airplane-types', AirplaneTypeViewSet)
router.register(r'airplanes', AirplaneViewSet)
router.register(r'flights', FlightViewSet)
router.register(r'crew', CrewViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'tickets', TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
