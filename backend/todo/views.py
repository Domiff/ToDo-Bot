from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import (
    TaskCreateSerializer,
    TaskDetailSerializer,
    TaskListSerializer,
    TaskUpdateSerializer,
)


class TodoListView(ListAPIView):
    serializer_class = TaskListSerializer
    permission_classes = IsAuthenticated,

    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user)


class TodoDetailView(RetrieveAPIView):
    serializer_class = TaskDetailSerializer

    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user)


class TodoCreateView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer


class TodoUpdateView(UpdateAPIView):
    serializer_class = TaskUpdateSerializer

    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user)


class TodoDeleteView(DestroyAPIView):
    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user)
