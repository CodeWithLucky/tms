from rest_framework import serializers
from . models import Label, Attachment, Task, Comment, TaskStage
from accounts.serializers import UserSerializer


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['label', 'color']

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['name']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['message']

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(many=True,read_only=True)
    labels = LabelSerializer(many=True,read_only=True)
    comments = serializers.SerializerMethodField()
    attachments = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'

    def get_comments(self, obj):
        comments = Comment.objects.filter(task=obj)
        return CommentSerializer(comments, many=True).data

    def get_attachments(self, obj):
        attachments = Attachment.objects.filter(task=obj)
        return AttachmentSerializer(attachments, many=True).data
    


class TaskStageSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()
    class Meta:
        model = TaskStage
        fields = '__all__'

    def get_tasks(self, obj):
        tasks = Task.objects.filter(task_stage = obj)
        return TaskSerializer(tasks, many = True).data

    