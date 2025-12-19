from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import ProfileSerializer


class RegisterAPIView(CreateAPIView):
    serializer_class = ProfileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.to_representation(user))
