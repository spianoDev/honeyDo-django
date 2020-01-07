from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name = 'todo_list'),
    path('todo/<int:pk>', views.todo_detail, name = 'todo_detail'),
    path('items/', views.item_list, name = 'item_list'),
    path('item/<int:pk>', views.item_detail, name = 'item_detail'),
    path('todo/new', views.todo_create, name = 'todo_create'),
    path('item/new', views.item_create, name = 'item_create'),
    path('todo/<int:pk>/update', views.todo_update, name = 'todo_update'),
    path('item/<int:pk>/update', views.item_update, name = 'item_update'),
    path('todo/<int:pk>/delete', views.todo_delete, name = 'todo_delete'),
    path('item/<int:pk>/delete', views.item_delete, name = 'item_delete'),
]
