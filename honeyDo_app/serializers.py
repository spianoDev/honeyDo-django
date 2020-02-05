from rest_framework import serializers
from .models import Todo, Item

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ['id', 'title', 'date', 'person',]

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id', 'task', 'todo',]
