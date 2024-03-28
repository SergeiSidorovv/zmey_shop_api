from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db.models.manager import BaseManager

from goods_favourite.services import favourite_services
from goods_favourite.models import Favourite
from goods_favourite import serializers, paginations


class FavouriteGoodsReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    """Gives out product cards, which added to the favourite user's, with the ability to view only"""

    serializer_class = serializers.GoodsFavourtieWithGoodsSerializer
    pagination_class = paginations.GoodsFavouritePaginations

    def get_queryset(self) -> BaseManager[Favourite]:
        """The function returns a list of products, which added to the favourite user's"""

        favourite_goods = favourite_services.get_favourite_goods(self.request.user.id)

        return favourite_goods


class FavouriteGooddsDeleteApiView(generics.DestroyAPIView):
    def get_queryset(self):
        favourite_goods = favourite_services.get_favourite_goods(self.request.user.id)
        return favourite_goods

    def delete(self, request, *args, **kwargs):

        id_product = self.kwargs["pk"]
        user_id = request.user.id

        favourite_product = favourite_services.get_favourite_product_by_id(
            user_id, id_product
        )
        if not favourite_product:
            return Response(
                "Такого товара не существует!", status=status.HTTP_400_BAD_REQUEST
            )
        return self.destroy(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("Товар успешно удалён!", status=status.HTTP_204_NO_CONTENT)


class FavouriteGooddsCreateApiView(generics.CreateAPIView):

    serializer_class = serializers.FavouriteGoodsSerializer

    def post(self, request, *args, **kwargs):

        favourite_product = favourite_services.get_favourite_product(
            request.user.id, int(request.data["goods"])
        )
        if favourite_product:
            return Response(
                "Такой товар в избранном уже есть!", status=status.HTTP_400_BAD_REQUEST
            )
        return self.create(request, *args, **kwargs)
