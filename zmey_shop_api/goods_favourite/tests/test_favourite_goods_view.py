from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status

from goods_favourite.models import Favourite
from goods_favourite.serializers import GoodsFavourtieSerializer
from goods_favourite.views import FavouriteGoodsReadOnlyModelViewSet
from goods_favourite.paginations import GoodsFavouritePaginations
from goods.models import Goods


class FavouriteGoodsReadOnlyModelViewSetTestCase(APITestCase):
    """A tests for views FavouriteGoodsReadOnlyModelViewSet"""

    def setUp(self):
        self.user = User.objects.create(username="user")
        product=Goods.objects.create(
            name="кардиган",
            main_photo="media/main_photo/name",
            description="Описание товара",
            slug="kardigan",
        )
        Favourite.objects.create(
            goods=product,
            user=self.user
        )

    def test_get_request(self):
        """Ensure we can get correct status code"""

        response = self.client.get("/api/v2/favourite_goods/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_serializer_class(self):
        """Ensure we can get correct serializer class"""

        expected_class = GoodsFavourtieSerializer
        serializer_class = FavouriteGoodsReadOnlyModelViewSet.serializer_class

        self.assertEqual(expected_class, serializer_class)

    def test_get_pagination_class(self):
        """Ensure we can get correct pagination class"""

        expected_class = GoodsFavouritePaginations
        pagination_class = FavouriteGoodsReadOnlyModelViewSet.pagination_class

        self.assertEqual(expected_class, pagination_class)
    
    def test_get_count_pages(self):
        """Ensure we can get correct pagination"""

        expected_pagination = 15
        paginaton_on_class =FavouriteGoodsReadOnlyModelViewSet.pagination_class.page_size

        self.assertEqual(expected_pagination, paginaton_on_class)
    
    def test_get_queryset(self):
        """Ensure we can get correct queryset"""

        request = self.client.get("/api/v2/favourite_goods/")
        request.user = self.user
        goods_favourite_view = FavouriteGoodsReadOnlyModelViewSet()
        goods_favourite_view.setup(request=request)
        queryset_goods_favourite = goods_favourite_view.get_queryset()

        expected_data = Favourite.objects.filter(user=self.user)

        self.assertQuerysetEqual(expected_data, queryset_goods_favourite)