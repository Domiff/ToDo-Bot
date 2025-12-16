from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from .models import Task
from .serializers import (
    TaskCreateSerializer,
    TaskDetailSerializer,
    TaskListSerializer,
    TaskUpdateSerializer,
)


class TodoListView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer


class TodoDetailView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer


class TodoCreateView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer


class TodoUpdateView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskUpdateSerializer


class TodoDeleteView(DestroyAPIView):
    queryset = Task.objects.all()
