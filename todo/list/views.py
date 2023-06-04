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
