from rest_framework import serializers

from goods.models import Goods


class GoodsSerializer(serializers.ModelSerializer):
    """Serializer for replacing goods data"""

    class Meta:
        model = Goods
        fields = ["id", "name", "main_photo", "description", "slug"]
