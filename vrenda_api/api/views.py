from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Flow
from .serializer import FlowSerializer


@api_view()
def health_check(request):
    return Response({'message': 'OK'})


class FlowsViewSet(viewsets.ModelViewSet):
    queryset = Flow.objects.all()
    serializer_class = FlowSerializer
