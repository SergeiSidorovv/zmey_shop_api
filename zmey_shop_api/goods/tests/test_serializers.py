from rest_framework.test import APITestCase
from django.urls import reverse

from goods.models import Goods
from goods.serializers import AllGoodsSerializer


class AllGoodsSerializerTestCase(APITestCase):
    """A tests for serializer AllGoodsSerializer"""

    def test_get_data_serializer(self):
        """Ensure we can get correct data"""

        product_one = Goods.objects.create(
            name="кардиган красный",
            main_photo="media/main_photo/кардиган-красный",
            description="Описание товара",
            article=1000006,
            composition="Ткань",
            slug="kardigan-krasnyis",
        )

        serializer_data = AllGoodsSerializer([product_one], many=True).data

        expected_data = [
            {
                "id": product_one.id,
                "name": "кардиган красный",
                "main_photo": "/media/media/main_photo/%D0%BA%D0%B0%D1%80%D0%B4%D0%B8%D0%B3%D0%B0%D0%BD-%D0%BA%D1%80%D0%B0%D1%81%D0%BD%D1%8B%D0%B9",
                "description": "Описание товара",
                "slug": "kardigan-krasnyis",
            }
        ]

        self.assertEqual(expected_data, serializer_data)