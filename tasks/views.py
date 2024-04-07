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
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class Task_view(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


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