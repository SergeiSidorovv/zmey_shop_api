from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from goods.services import goods_services
from goods import serializers

class AllGoodsReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = goods_services.get_goods_for_product_card()
    serializer_class = serializers.AllGoodsSerializers