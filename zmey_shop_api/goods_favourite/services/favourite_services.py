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


def get_favourite_product_by_id_goods(
    user_id: int, id_goods: int
) -> BaseManager[Favourite]:
    """Gives the selected favourite product by goods id.

    Keyword arguments:
    user_id -- the ID of the registered user
    id_goods -- the ID of the product from goods table
    """

    favourite_product = Favourite.objects.filter(
        user_id=user_id, goods_id=id_goods
    ).only("goods")

    return favourite_product


def get_favourite_product_by_id(
    user_id: int, favourite_product_id: int
) -> BaseManager[Favourite]:
    """Gives the selected favourite product by product id.

    Keyword arguments:
    user_id -- the ID of the registered user
    id_product -- the ID of the product choice
    """

    favourite_product = Favourite.objects.filter(
        id=favourite_product_id, user_id=user_id
    ).only("id", "user", "goods")

    return favourite_product
