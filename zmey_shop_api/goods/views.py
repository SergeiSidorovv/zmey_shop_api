from rest_framework import viewsets

from goods.services import goods_services
from goods import serializers, paginations


class AllGoodsReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    """Shows product cards with the ability to view only"""

    queryset = goods_services.get_goods_data_for_product_cards()
    serializer_class = serializers.GoodsSerializer
    pagination_class = paginations.GoodsPaginations


class ChoiceGoodsModelViewSet(viewsets.ReadOnlyModelViewSet):
    """Shows product cards for the selected category slug with the ability to view"""

    serializer_class = serializers.GoodsSerializer
    pagination_class = paginations.GoodsPaginations

    def get_queryset(self):
        """The function returns a list of products by the selected category"""

        category_slug = self.kwargs["slug"]
        choice_product =  goods_services.get_goods_select_category(category_slug)
        return choice_product
        