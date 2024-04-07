from . serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from . models import CustomUser
from django.db import IntegrityError
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication

# Create your views here.
# @api_view(['POST'])
# def signup_view(request):
#     if request.method == 'POST':

#         email = request.data.get('email')
#         username = request.data.get('username')
#         password = request.data.get('password')

        
#         try:
#             user = CustomUser.objects.create_user(email = email , username=username, password = password)
#             if user:
#                 return Response({'message' : 'User created successfully'},status=status.HTTP_201_CREATED)
#         except IntegrityError:
#             return Response({'error' : 'username already exists'}, status= status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({'eUserrror' : f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        

class UserView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    class Meta:
        model = CustomUser
        fields = '__all__'
