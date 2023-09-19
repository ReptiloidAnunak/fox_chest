from rest_framework.serializers import ModelSerializer
from .models import TShort, Pants, Jacket, Bodysuit, Wear, Brand


class BrandCreateSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class TShortsListSerializer(ModelSerializer):
    class Meta:
        model = TShort
        exclude = ["id"]


class TShortsCreateSerializer(ModelSerializer):
    class Meta:
        model = TShort
        fields = "__all__"


class PantsListSerializer(ModelSerializer):
    class Meta:
        model = Pants
        exclude = ["id"]


class JacketsListSerializer(ModelSerializer):
    class Meta:
        model = Jacket
        exclude = ["id"]


class BodysuitListSerializer(ModelSerializer):
    class Meta:
        model = Bodysuit
        exclude = ["id"]