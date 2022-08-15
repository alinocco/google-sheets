from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r"orders", views.OrderViewSet, basename="orders")

urlpatterns = [
    path('', include(router.urls)),
    path('total-income/', views.serialize_total_income, name='total-income'),
]