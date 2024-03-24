from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from django.urls import reverse

from goods.models import Goods, CategoryGoods
from goods.views import ChoiceGoodsReadOnlyModelViewSet
from goods.serializers import GoodsSerializer
from goods.paginations import GoodsPaginations


class ChoiceGoodsReadOnlyModelViewSetTestCase(APITestCase):
    """A tests for views ChoiceGoodsReadOnlyModelViewSet"""

    def setUp(self):
        self.factory = APIRequestFactory()

        category = CategoryGoods.objects.create(
            name="Верхняя одежда",
            slug="Verhnya-odezda",
        )
        Goods.objects.create(
            name="кардиган красный",
            main_photo="media/main_photo/кардиган-красный",
            description="Описание товара",
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

    def test_get_request(self):
        """Ensure we can get correct status code"""

        url = reverse("choicegoods-list", kwargs={"slug": "кардиган"})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_serializer_class(self):
        """Ensure we can get correct serializer class"""

        expected_class = GoodsSerializer
        serializer_class = ChoiceGoodsReadOnlyModelViewSet.serializer_class

        self.assertEqual(expected_class, serializer_class)

    def test_get_pagination_class(self):
        """Ensure we can get correct pagination class"""

        expected_class = GoodsPaginations
        serializer_class = ChoiceGoodsReadOnlyModelViewSet.pagination_class

        self.assertEqual(expected_class, serializer_class)

    def test_get_count_pages(self):
        """Ensure we can get correct pagination"""

        expected_pagination = 15
        paginaton_on_class = ChoiceGoodsReadOnlyModelViewSet.pagination_class.page_size

        self.assertEqual(expected_pagination, paginaton_on_class)

    def test_get_queryset(self):
        """Ensure we can get correct queryset"""

        request = self.factory.get(
            reverse("choicegoods-list", kwargs={"slug": "Verhnya-odezda"})
        )

        choice_godos_view = ChoiceGoodsReadOnlyModelViewSet()
        choice_godos_view.setup(request, slug="Verhnya-odezda")
        queryset_choice_goods = choice_godos_view.get_queryset()

        choice_category = CategoryGoods.objects.first()
        choice_goods = Goods.objects.filter(category=choice_category.id)

        self.assertQuerysetEqual(queryset_choice_goods, choice_goods)
