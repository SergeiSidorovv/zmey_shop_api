from rest_framework import viewsets

from goods.services import goods_services
from goods import serializers, paginations


class AllGoodsReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    """A ViewSet for viewing all goods with only read"""

    queryset = goods_services.get_goods_data_for_product_cards()
    serializer_class = serializers.AllGoodsSerializer
    pagination_class = paginations.GoodsPaginations
