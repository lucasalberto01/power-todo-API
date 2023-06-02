from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListTodo.as_view(), name="list-list"),
]
