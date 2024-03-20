from rest_framework import serializers

from goods.models import Goods


class AllGoodsSerializer(serializers.ModelSerializer):
    """A serializer for changes goods data"""

    class Meta:
        model = Goods
        fields = ["id", "name", "main_photo", "description", "slug"]