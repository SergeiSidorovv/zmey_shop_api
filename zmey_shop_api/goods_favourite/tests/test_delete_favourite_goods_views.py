from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

from goods_favourite.serializers import FavouriteGoodsSerializer
from goods_favourite.views import FavouriteGooddsDeleteApiView
from goods_favourite.paginations import GoodsFavouritePaginations
from goods_favourite.models import Favourite
from goods.models import Goods


class FavouriteGooddsDeleteApiViewTestCase(APITestCase):
    """A tests for views FavouriteGooddsDeleteApiView"""

    def setUp(self):
        self.user = User.objects.create(username="user")
        product = Goods.objects.create(
            name="кардиган",
            main_photo="media/main_photo/name",
            description="Описание товара",
            slug="kardigan",
        )

        Favourite.objects.create(goods=product, user=self.user)

    def test_get_request(self):
        """Ensure we can get correct status code"""

        response = self.client.delete("/api/v2/delete/1")

        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_get_queryset(self):
        """Ensure we can get correct queryset"""

        request = self.client.delete("/api/v2/delete/1/")
        request.user = self.user
        delete_favourite_view = FavouriteGooddsDeleteApiView()
        pk_favourite = 1
        delete_favourite_view.setup(request=request, pk=pk_favourite)
        query_set_delete_favourite = delete_favourite_view.get_queryset()

        expected_data = Favourite.objects.filter(
            id=pk_favourite, user_id=request.user
        ).only("id", "user", "goods")

        self.assertQuerysetEqual(expected_data, query_set_delete_favourite)
