from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import TgProfile


class ProfileSerializer(serializers.Serializer):
    tg_id = serializers.IntegerField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def create(self, validated_data):
        tg_id = validated_data["tg_id"]
        tg_profile = TgProfile.objects.filter(tg_id=tg_id).select_related("user").first()

        if tg_profile:
            user = tg_profile.user
        else:
            user = User.objects.create_user(username=f"tg-{tg_id}")
            tg_profile = TgProfile.objects.create(user=user, **validated_data)
        return user

    def to_representation(self, user):
        tokens = RefreshToken.for_user(user)
        return {
            "id": user.id,
            "tokens": {
                "refresh": str(tokens),
                "access": str(tokens.access_token),
            }
        }
