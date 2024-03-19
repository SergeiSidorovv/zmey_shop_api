from rest_framework import serializers

from goods.models import Goods


class AllGoodsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ["id", "name", "main_photo", "description", "slug"]