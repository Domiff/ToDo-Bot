from adrf.serializers import ModelSerializer

from ..models import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "urgency"
