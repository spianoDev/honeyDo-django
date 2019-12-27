from django.db import models
from datetime import date

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=180)
    date = models.DateField(auto_now=False, auto_now_add=False, default=date.today)
    person = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Item(models.Model):
    name = models.CharField(default='', max_length=300)
    task = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.name
