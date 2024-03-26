from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from django.urls import reverse

from goods.models import Goods
from goods.views import AllGoodsReadOnlyModelViewSet
from goods.serializers import GoodsSerializer
from goods.paginations import GoodsPaginations


class AllGoodsReadOnlyModelViewSetTestCase(APITestCase):
    """A tests for views AllGoodsReadOnlyViewSet"""

    def setUp(self):
        self.factory = APIRequestFactory()

        Goods.objects.create(
            name="кардиган",
            main_photo="media/main_photo/name",
            description="Описание товара",
            slug="kardigan",
        )
        Goods.objects.create(
            name="шапка",
            main_photo="media/main_photo/name2",
            description="Описание товара2",
            slug="shapka",
        )
        Goods.objects.create(
            name="шарф красный",
            main_photo="media/main_photo/шарф-красный",
            description="Описание товара3",
            slug="sharf-krasnyi",
        )

    def test_get_request(self):
        """Ensure we can get correct status code"""

        response = self.client.get("/api/v1/allgoods/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_serializer_class(self):
        """Ensure we can get correct serializer class"""

        expected_class = GoodsSerializer
        serializer_class = AllGoodsReadOnlyModelViewSet.serializer_class

        self.assertEqual(expected_class, serializer_class)

    def test_get_pagination_class(self):
        """Ensure we can get correct pagination class"""

        expected_class = GoodsPaginations
        pagination_class = AllGoodsReadOnlyModelViewSet.pagination_class

        self.assertEqual(expected_class, pagination_class)

    def test_get_count_pages(self):
        """Ensure we can get correct pagination"""

        expected_pagination = 15
        paginaton_on_class = AllGoodsReadOnlyModelViewSet.pagination_class.page_size

        self.assertEqual(expected_pagination, paginaton_on_class)

    def test_get_queryset(self):
        """Ensure we can get correct queryset"""

        queryset = AllGoodsReadOnlyModelViewSet.queryset
        expected_data = Goods.objects.only(
            "id", "name", "main_photo", "description", "slug"
        )

        self.assertQuerysetEqual(expected_data, queryset)
