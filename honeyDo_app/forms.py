from django import forms
from .models import Todo, Item

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('title', 'date', 'person',)

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('task', 'todo',)
