from django.shortcuts import render
from .models import Todo, Item

# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = Todo.objects.get(id = pk)
    return render(request, 'todo_detail.html', {'todo': todo})
