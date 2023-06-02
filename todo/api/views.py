from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from .models import Task


class TaskTodo(APIView):
    """Routes for the API without id"""
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get(self, request):
        id = request.user.id
        tasks = Task.objects.filter(
            by_list__user_id=id
        )
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class TaskTodoById(APIView):
    """Routes for the API with id"""
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        tasks = Task.objects.get(id=pk)
        serializer = TaskSerializer(tasks, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        task = Task.objects.get(id=pk)
        task.delete()
        return Response("Tasks deleted successfully.")
