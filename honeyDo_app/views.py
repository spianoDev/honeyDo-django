from django.shortcuts import render
from .models import Todo, Item

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = Todo.objects.get(id = pk)
    return render(request, 'todo_detail.html', {'todo': todo})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def item_detail(request, pk):
    item = Item.objects.get(id = pk)
    return render(request, 'item_detail.html', {'item': item})
