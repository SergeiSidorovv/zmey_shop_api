from rest_framework.test import APITestCase

from goods.models import Goods, CategoryGoods
from goods.services import goods_services


class GoodsServicesTestCase(APITestCase):
    """A tests for functions in goods_services file"""

    def setUp(self):
        category = CategoryGoods.objects.create(
            name="Шарф",
            slug="Sharf",
        )
        Goods.objects.create(
            name="кардиган красный",
            main_photo="media/main_photo/кардиган-красный",
            description="Описание товара",
            article=1000001,
            slug="kardigan-krasnyi",
            category=category,
        )
        Goods.objects.create(
            name="шапка",
            main_photo="media/main_photo/name2",
            description="Описание товара2",
            composition="Хлопок",
            slug="shapka",
            category=category,
        )
        Goods.objects.create(
            name="шарф красный",
            main_photo="media/main_photo/шарф-красный",
            description="Описание товара3",
            additional_materials="нет",
            slug="sharf-krasnyi",
            category=category,
        )

    def test_data_from_get_goods_data_for_product_cards(self):
        """Ensure we can get correct data from function get_goods_data_for_product_cards"""

        expected_data = Goods.objects.only(
            "id", "name", "main_photo", "description", "slug"
        )
        function_data = goods_services.get_goods_data_for_product_cards()

        self.assertQuerysetEqual(expected_data, function_data)

    def test_data_from_get_search_goods(self):
        """Ensure we can get correct data from function get_search_goods"""

        name_product = "кардиган"
        expected_data = Goods.objects.filter(name__icontains=name_product).only(
            "id", "name", "main_photo", "description", "slug"
        )
        function_data = goods_services.get_search_goods(name_product=name_product)

        self.assertQuerysetEqual(expected_data, function_data)

    def test_data_from_get_goods_select_category(self):
        """Ensure we can get correct data from function get_goods_select_category"""

        category = CategoryGoods.objects.first()
        expected_data = Goods.objects.filter(category=category.id).only(
            "id", "name", "main_photo", "description", "slug"
        )

        category_name = "Sharf"
        function_data = goods_services.get_goods_select_category(
            category_slug=category_name
        )

        self.assertQuerysetEqual(expected_data, function_data)
