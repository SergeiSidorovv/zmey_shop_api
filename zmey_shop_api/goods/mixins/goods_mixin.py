from goods import serializers, paginations


class BaseDataMixin:
    """Gives out base criteria for classes from views goods. The Class has serializer_class and
    pagination_class
    """

    serializer_class = serializers.GoodsSerializer
    pagination_class = paginations.GoodsPaginations
