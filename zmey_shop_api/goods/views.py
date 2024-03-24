from rest_framework import viewsets
from django.db.models.manager import BaseManager

from goods.services import goods_services
from goods import serializers, paginations
from goods.models import Goods


class AllGoodsReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    """Gives out product cards with the ability to view only"""

    queryset = goods_services.get_goods_data_for_product_cards()
    serializer_class = serializers.GoodsSerializer
    pagination_class = paginations.GoodsPaginations


class ChoiceGoodsReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    """Gives out  product cards for the selected category slug with the ability to view"""

    serializer_class = serializers.GoodsSerializer
    pagination_class = paginations.GoodsPaginations

    def get_queryset(self) -> BaseManager[Goods]:
        """The function returns a list of products by the selected category"""

        category_slug = self.kwargs["slug"]
        choice_product = goods_services.get_goods_select_category(category_slug)
        return choice_product


class SearchGoodsReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    """Gives out product cards for the desired product name with the ability to view"""

    serializer_class = serializers.GoodsSerializer
    pagination_class = paginations.GoodsPaginations

    def get_queryset(self) -> BaseManager[Goods]:
        """The function returns a list of products by the desired product name"""

        if not self.request.GET.get("search_form"):
            empty_name = ""
            search_goods = goods_services.get_search_goods(empty_name)
            return search_goods

        search_goods = goods_services.get_search_goods(
            self.request.GET.get("search_form")
        )

        return search_goods
