from . serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from . models import CustomUser
from django.db import IntegrityError
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import get_user_model


CustomUser = get_user_model()

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
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return CustomUser.objects.all()
        elif user.is_staff or user.is_active:
            return CustomUser.objects.filter(pk=user.pk)
        else:
            return CustomUser.objects.none()  # or any other default behavior


    def retrieve(self, request, *args, **kwargs):
        serializer = UserSerializer(self.request.data)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        print(request.data)
        email = request.data.get('email')
        username = request.data.get('username')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        user = CustomUser.objects.create_user(email = email, username=username, password=password, first_name=first_name, last_name=last_name)
        if user:
            return super().create(request, *args, **kwargs)
        else:
            return Response({'error' : 'Failed to create user'}, status=status.HTTP_400_BAD_REQUEST)
        

    class Meta:
        model = CustomUser
        fields = '__all__'

