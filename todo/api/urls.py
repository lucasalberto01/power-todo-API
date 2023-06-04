from django.urls import path
from . import views

urlpatterns = [
    path('<str:pk>/', views.TaskTodoById.as_view(), name="task-detail"),
]
