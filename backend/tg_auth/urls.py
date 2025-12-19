from django.urls import path

from .views import RegisterAPIView


app_name = "tg_auth"

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
]
