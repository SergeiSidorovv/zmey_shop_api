from rest_framework import routers

from goods import views

router_goods = routers.SimpleRouter()

router_goods.register(r'allgoods',views.AllGoodsReadOnlyViewSet, basename='allgoods')

