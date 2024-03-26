from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from django.urls import reverse

from goods.models import Goods
from goods.views import SearchGoodsReadOnlyModelViewSet
from goods.serializers import GoodsSerializer
from goods.paginations import GoodsPaginations


class SearchGoodsReadOnlyModelViewSetTestCase(APITestCase):
    """A tests for views SearchGoodsReadOnlyModelViewSet"""

    def setUp(self):
        self.factory = APIRequestFactory()

        Goods.objects.create(
            name="кардиган красный",
            main_photo="media/main_photo/кардиган-красный",
            description="Описание товара",
            article=1000009,
            slug="kardigan-krasnyi",
        )
        Goods.objects.create(
            name="шапка",
            main_photo="media/main_photo/name2",
            description="Описание товара2",
            composition="Хлопок",
            article=10000010,
            slug="shapka",
        )
        Goods.objects.create(
            name="шарф красный",
            main_photo="media/main_photo/шарф-красный",
            description="Описание товара3",
            additional_materials="нет",
            slug="sharf-krasnyi",
        )

    def test_get_request(self):
        """Ensure we can get correct status code"""

        response = self.client.get("/api/v1/search/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_serializer_class(self):
        """Ensure we can get correct serializer class"""

        expected_class = GoodsSerializer
        serializer_class = SearchGoodsReadOnlyModelViewSet.serializer_class

        self.assertEqual(expected_class, serializer_class)

    def test_get_pagination_class(self):
        """Ensure we can get correct pagination class"""

        expected_class = GoodsPaginations
        serializer_class = SearchGoodsReadOnlyModelViewSet.pagination_class

        self.assertEqual(expected_class, serializer_class)

    def test_get_count_pages(self):
        """Ensure we can get correct pagination"""

        expected_pagination = 15
        paginaton_on_class = SearchGoodsReadOnlyModelViewSet.pagination_class.page_size

        self.assertEqual(expected_pagination, paginaton_on_class)

    def test_get_queryset(self):
        """Ensure we can get correct queryset"""

        request = self.factory.get("search", {"search_form": "кардиган"})

        search_goods_view = SearchGoodsReadOnlyModelViewSet()
        search_goods_view.setup(request=request)
        queryset_serch_goods = search_goods_view.get_queryset()

        name_product = "кардиган"
        expected_data = Goods.objects.filter(name__icontains=name_product).only(
            "id", "name", "main_photo", "description", "slug"
        )

        self.assertQuerysetEqual(expected_data, queryset_serch_goods)
