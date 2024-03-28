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

        user_id = self.request.user.id
        favourite_goods = favourite_services.get_favourite_goods(user_id)
        return favourite_goods


class FavouriteGooddsDeleteApiView(generics.DestroyAPIView):
    """Delete product by the id product from the favourite"""

    def get_queryset(self):
        """
        The function returns the product by id, which will be deleted to the favourite
        database
        """

        id_product = self.kwargs["pk"]
        user_id = self.request.user.id

        favourite_product = favourite_services.get_favourite_product_by_id(
            user_id, id_product
        )
        return favourite_product

    def destroy(self, request, *args, **kwargs):
        """Destroy a model instance"""

        instance = self.get_object()
        self.perform_destroy(instance)
        return Response("Товар успешно удалён!", status=status.HTTP_204_NO_CONTENT)


class FavouriteGooddsCreateApiView(generics.CreateAPIView):
    """Add product by the id goods from the favourite"""

    serializer_class = serializers.FavouriteGoodsSerializer

    def post(self, request, *args, **kwargs):
        """
        The function will be added the product by id goods to the favourite database,
        or returns Response(status)
        """

        user_id = request.user.id
        goods_id = int(request.data["goods"])

        favourite_product = favourite_services.get_favourite_product_by_id_goods(
            user_id, goods_id
        )
        if favourite_product:
            return Response(
                "Такой товар в избранном уже есть!", status=status.HTTP_400_BAD_REQUEST
            )
        return self.create(request, *args, **kwargs)
