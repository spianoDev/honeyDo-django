from django.shortcuts import render, redirect
from .models import Todo, Item
from .forms import TodoForm, ItemForm
from rest_framework import generics
from .serializers import TodoSerializer, ItemSerializer

# Create your views here.
class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = Todo.objects.get(id = pk)
    return render(request, 'todo_detail.html', {'todo': todo})

def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm()
    return render(request, 'todo_form.html', {'form': form})

def todo_update(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo_form.html', {'form': form})

def todo_delete(request, pk):
    Todo.objects.get(id=pk).delete()
    return redirect('todo_list')

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def item_detail(request, pk):
    item = Item.objects.get(id = pk)
    return render(request, 'item_detail.html', {'item': item})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('todo_detail', pk = item.todo.pk)
    else:
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form})

def item_update(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return redirect('todo_detail', pk = item.todo.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_form.html', {'form': form})

def item_delete(request, pk):
    item = Item.objects.get(pk=pk)
    parent_id = item.todo.pk
    item.delete()
    return redirect('todo_detail', pk = parent_id)
