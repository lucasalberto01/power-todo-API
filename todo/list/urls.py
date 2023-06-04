from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListTodo.as_view(), name="list-list"),
    path('<int:pk>/', views.ListTodoManager.as_view(), name="list-manager")
]
