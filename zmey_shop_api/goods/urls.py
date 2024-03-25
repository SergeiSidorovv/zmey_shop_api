from rest_framework import routers
from django.urls import path, include

from goods import views

router_goods = routers.SimpleRouter()

router_goods.register(
    r"allgoods", views.AllGoodsReadOnlyModelViewSet, basename="allgoods"
)
router_goods.register(
    r"choicegoods/(?P<slug>[\w-]+)",
    views.ChoiceGoodsReadOnlyModelViewSet,
    basename="choicegoods",
)
router_goods.register(
    r"search", views.SearchGoodsReadOnlyModelViewSet, basename="search"
)

urlpatterns = [
    path(r"", include((router_goods.urls, ".goods.urls"))),
]
