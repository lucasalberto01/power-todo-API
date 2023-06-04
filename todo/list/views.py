import random
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import List
from .serializers import ListSerializer

logger = logging.getLogger(__name__)


def getRandomColor():
    return "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])


class ListTodo(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListSerializer

    def get(self, request):
        id = request.user.id
        print(id)
        tasks = List.objects.filter(user_id=id)
        serializer = ListSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        user_id = request.user.id

        serializer = ListSerializer(
            data={'user_id': user_id,
                  'name': request.data['name'],
                  'color': getRandomColor()
                  }
        )
        if serializer.is_valid():
            serializer.save(user_id=request.user)
        return Response(serializer.data)


class ListTodoManager(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListSerializer

    def delete(self, request, pk):
        user_id = request.user.id
        is_permitted = List.objects.filter(id=pk, user_id=user_id).exists()

        if not is_permitted:
            return Response({"message": "You are not permitted to delete this task."}, status=403)

        List.objects.filter(id=pk).delete()
        return Response({"message": "Task with id `{}` has been deleted.".format(id)}, status=204)

    def put(self, request, pk):
        user_id = request.user.id
        is_permitted = List.objects.filter(id=pk, user_id=user_id).exists()

        if not is_permitted:
            return Response({"message": "You are not permitted to update this task."}, status=403)

        task = List.objects.get(id=pk)
        serializer = ListSerializer(
            instance=task, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=400)
