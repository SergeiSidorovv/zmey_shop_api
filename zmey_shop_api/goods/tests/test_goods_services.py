from rest_framework.test import APITestCase

from goods.models import Goods
from goods.services import goods_services


class GoodsServicesTestCase(APITestCase):
    """A tests for functions in goods_services file"""

    def setUp(self):
        Goods.objects.create(
            name="кардиган красный",
            main_photo="media/main_photo/кардиган-красный",
            description="Описание товара",
            article = 1000001,
            slug="kardigan-krasnyi",
        )
        Goods.objects.create(
            name="шапка",
            main_photo="media/main_photo/name2",
            description="Описание товара2",
            composition = "Хлопок",
            slug="shapka",
        )
        Goods.objects.create(
            name="шарф красный",
            main_photo="media/main_photo/шарф-красный",
            description="Описание товара3",
            additional_materials = "нет",
            slug="sharf-krasnyi",
        )


    def test_data_from_get_goods_data_for_product_cards(self):
        """Ensure we can get correct data from function get_goods_data_for_product_cards"""

        expected_data = Goods.objects.only("id", "name", "main_photo", "description", "slug")
        function_data = goods_services.get_goods_data_for_product_cards()

        self.assertQuerysetEqual(expected_data, function_data)