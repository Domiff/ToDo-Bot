from django.contrib.auth.models import User
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from ..models import Category, Task


class TaskBaseSerializer(ModelSerializer):
    category = SlugRelatedField(
        slug_field="urgency",
        queryset=Category.objects.all(),
    )
    creator = SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all(),
    )

    class Meta:
        model = Task
        fields = (
            "creator",
            "title",
            "deadline",
            "category",
        )


class TaskListSerializer(TaskBaseSerializer):
    class Meta(TaskBaseSerializer.Meta):
        fields = TaskBaseSerializer.Meta.fields + ("body", "completed")


class TaskDetailSerializer(TaskBaseSerializer):
    class Meta(TaskBaseSerializer.Meta):
        fields = TaskBaseSerializer.Meta.fields + (
            "body",
            "completed",
            "created_at",
            "updated_at",
        )


class TaskCreateSerializer(TaskBaseSerializer):
    class Meta(TaskBaseSerializer.Meta):
        fields = TaskBaseSerializer.Meta.fields + ("body",)


class TaskUpdateSerializer(TaskBaseSerializer):
    class Meta(TaskBaseSerializer.Meta):
        fields = TaskBaseSerializer.Meta.fields + ("body", "deadline", "completed")
