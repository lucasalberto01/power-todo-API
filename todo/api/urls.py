from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskTodo.as_view(), name="task-list"),
    path('<str:pk>/', views.TaskTodoById.as_view(), name="task-detail"),
]
