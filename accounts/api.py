## views

from .models import Login
from .serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])

def login_api(request):

    all_fields = Login.objects.all()
    data = LoginSerializer(all_fields, many=True).data

    return Response({'data':data})