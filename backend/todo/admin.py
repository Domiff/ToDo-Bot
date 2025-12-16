from django.contrib import admin

from .models import Category, Task


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("urgency",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "creator",
        "title",
        "completed",
        "created_at",
        "updated_at",
        "deadline",
        "category",
    )
    list_editable = (
        "title",
        "completed",
    )
