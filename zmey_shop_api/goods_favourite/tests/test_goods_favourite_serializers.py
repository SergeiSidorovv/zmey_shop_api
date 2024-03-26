from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from goods_favourite.models import Favourite
from goods_favourite.serializers import GoodsFavourtieSerializer
from goods.models import Goods


class GoodsFavouriteSerializerTestCase(APITestCase):
    """A tests for serializer GoodsFavouriteSerializer"""

    def test_get_data_serializer(self):
        """Ensure we can get correct data"""

        self.user = User.objects.create(username="user")
        product = Goods.objects.create(
            name="кардиган",
            main_photo="media/main_photo/name",
            description="Описание товара",
            slug="kardigan",
        )
        favourite_goods = Favourite.objects.create(goods=product, user=self.user)

        serializer_data = GoodsFavourtieSerializer([favourite_goods], many=True).data

        expected_data = [
            {
                "goods": {
                    "id": product.id,
                    "name": "кардиган",
                    "main_photo": "/media/media/main_photo/name",
                    "description": "Описание товара",
                    "slug": "kardigan",
                }
            }
        ]

        self.assertEqual(expected_data, serializer_data)
