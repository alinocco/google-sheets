from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Order
from .serializers import OrderSerializer

from ..services.statistics import get_total_income

class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

@api_view(['GET'])
def serialize_total_income(request):
    total_income = get_total_income()

    return Response({'total_income': total_income})




