from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from . models import Label, Comment, Task, TaskStage, Attachment
from . serializers import  LabelSerializer, CommentSerializer, TaskSerializer, TaskStageSerializer, AttachmentSerializer
from rest_framework.authentication import SessionAuthentication

# Create your views here.
class Label_view(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class Comment_view(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def list(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many = True)
        return Response(serializer.data)


class Task_view(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return Task.objects.all()
        if user.is_staff:
            return Task.objects.filter(assign_to = user, assign_by = user)
        return super().get_queryset()
    

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)
    

    def list(self, request):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many = True)
        return Response(serializer.data)


class TaskStage_view(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    queryset = TaskStage.objects.all()
    serializer_class = TaskStageSerializer

class Attachment_view(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer