from rest_framework import serializers
from .models import Todo, Item

class TodoSerializer(serializers.HyperlinkedModelSerializer):

    todo_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'todo_detail'
    )
    class Meta:
        model = Todo
        fields = ['id', 'title', 'date', 'person', 'todo_url',]

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id', 'task', 'todo',]
