from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse
from rest_framework import status

from goods.models import Goods, CategoryGoods
from goods.views import AllGoodsReadOnlyViewSet
from goods.serializers import AllGoodsSerializer
from goods.paginations import GoodsPaginations


class AllGoodsViewSetTestCase(APITestCase):
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

        url = reverse("allgoods-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_queryset(self):
        """Ensure we can get correct queryset"""

        queryset = AllGoodsReadOnlyViewSet.queryset
        expected_data = Goods.objects.only("id", "name", "main_photo", "description", "slug")

        self.assertQuerysetEqual(expected_data, queryset)

    def test_get_serializer_class(self):
        """Ensure we can get correct serializer class"""

        expected_class = AllGoodsSerializer
        serializer_class = AllGoodsReadOnlyViewSet.serializer_class

        self.assertEqual(expected_class, serializer_class)
    
    def test_get_pagination_class(self):
        """Ensure we can get correct pagination class"""

        expected_class = GoodsPaginations
        serializer_class = AllGoodsReadOnlyViewSet.pagination_class

        self.assertEqual(expected_class, serializer_class)

    def test_get_count_pages(self):
        """Ensure we can get correct pagination"""

        expected_pagination = 15
        paginaton_on_class = AllGoodsReadOnlyViewSet.pagination_class.page_size

        self.assertEqual(expected_pagination, paginaton_on_class)
    
