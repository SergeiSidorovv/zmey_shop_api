from rest_framework import routers

from goods import views

router_goods = routers.SimpleRouter()

router_goods.register(r"allgoods", views.AllGoodsReadOnlyViewSet, basename="allgoods")
router_goods.register(r"choicegoods/(?P<slug>[\w-]+)", views.ChoiceGoodsModelViewSet, basename="choicegoods")
