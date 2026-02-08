from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from adrf.generics import CreateAPIView

from .serializers import ProfileSerializer


class RegisterAPIView(CreateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = AllowAny,

    async def create(self, request, *args, **kwargs):
        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = await serializer.ato_representation(user)
        return Response(data, status=status.HTTP_201_CREATED)
