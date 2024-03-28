from rest_framework import serializers

from goods_favourite.models import Favourite
from goods.serializers import GoodsSerializer


class GoodsFavourtieWithGoodsSerializer(serializers.ModelSerializer):
    """Serializer for replacing favourite goods data"""

    goods = GoodsSerializer(read_only=True)

    class Meta:
        """Metadata by favourite goods serializer"""

        model = Favourite
        fields = ["goods"]


class FavouriteGoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favourite
        fields = ["id", "user", "goods"]