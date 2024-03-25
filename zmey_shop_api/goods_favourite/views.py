from rest_framework import viewsets
from django.db.models.manager import BaseManager

from goods_favourite.services import favourite_services
from goods_favourite.models import Favourite
from goods_favourite import serializers, paginations


class FavouriteGoodsReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    """Gives out product cards, which added to the favourite user's, with the ability to view only"""

    serializer_class = serializers.GoodsFavourtieSerializer
    pagination_class = paginations.GoodsFavouritePaginations

    def get_queryset(self) -> BaseManager[Favourite]:
        """The function returns a list of products, which added to the favourite user's"""

        favourite_goods = favourite_services.get_favourite_goods(self.request.user.id)

        return favourite_goods
