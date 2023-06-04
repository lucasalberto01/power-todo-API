from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from .models import Task


@api_view(['GET'])
def apiOverview(request):
    return Response({"runnig": "true"})


class TaskTodoById(APIView):
    """Routes for the API with id"""
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def post(self, request, pk):
        data = {
            'title': request.data['title'],
            'completed': request.data['completed'] if 'completed' in request.data else False,
            'by_list': pk
        }
        print(data)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            print("SAVED TASK")
            serializer.save()
            return Response(serializer.data)
        else:
            print("ERROR")
            return Response(serializer.errors, 400)

    def get(self, request, pk):
        tasks = Task.objects.filter(by_list_id=pk)
        serializer = TaskSerializer(tasks, many=True)
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
