from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def health_check(request):
    return Response({'message': 'OK'})
