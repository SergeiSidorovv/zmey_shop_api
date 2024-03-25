from rest_framework import routers
from django.urls import path, include

from goods_favourite import views


router_goods_favourite = routers.SimpleRouter()

router_goods_favourite.register(
    r"favourite_goods",
    views.FavouriteGoodsReadOnlyModelViewSet,
    basename="favourite_goods",
)

urlpatterns = [
    path("", include((router_goods_favourite.urls, "goods_favourite.urls"))),
]
