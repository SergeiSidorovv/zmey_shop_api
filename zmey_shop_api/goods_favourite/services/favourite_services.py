from django.db.models.manager import BaseManager
from django.db.models import Prefetch

from goods_favourite.models import Favourite
from goods.models import Goods


def get_favourite_goods(user_id: int) -> BaseManager[Favourite]:
    """A function for getting goods, which save  to the favourite goods database

    Keyword arguments:
    user_id -- ID of the registered user to the finding favourite goods
    """

    favourite_goods = (
        Favourite.objects.filter(user_id=user_id)
        .only("goods")
        .prefetch_related(
            Prefetch(
                "goods",
                queryset=Goods.objects.only(
                    "id", "name", "main_photo", "description", "slug"
                ),
            )
        )
    )

    return favourite_goods
