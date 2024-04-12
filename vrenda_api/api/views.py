from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Flow
from .serializer import FlowSerializer


@api_view()
def health_check(request):
    return Response({'message': 'OK'})


class FlowsViewSet(viewsets.ViewSet):
    queryset = Flow.objects.all()
    serializer_class = FlowSerializer

    def list(self, request):
        queryset = Flow.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
