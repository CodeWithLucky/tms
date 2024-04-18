from django.contrib.auth.models import User
from . models import Work
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model : Work
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def get_work(self, obj):
        work_list = []
        if obj:
            works = Work.objects.filter(user = obj)

            for work in works:
                work_list.append(work.title)
        return work_list