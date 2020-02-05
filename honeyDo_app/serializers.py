from rest_framework import serializers
from .models import Todo, Item

class TodoSerializer(serializers.HyperlinkedModelSerializer):

    tasks = serializers.HyperlinkedRelatedField(
        view_name = 'item_detail',
        many = True,
        read_only = True
    )
    todo_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'todo_detail'
    )
    class Meta:
        model = Todo
        fields = ['id', 'title', 'date', 'person', 'todo_url', 'tasks']

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id', 'task', 'todo',]
