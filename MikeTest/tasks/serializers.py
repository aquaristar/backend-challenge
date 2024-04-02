from rest_framework import serializers
from .models import Task, Label
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Task
        fields = ('task_id', 'title', 'description', 'task_status', 'owner')


class LabelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Label
        fields = ('label_id', 'name', 'owner')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer user model
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
    labels = serializers.PrimaryKeyRelatedField(many=True, queryset=Label.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'tasks', 'labels')