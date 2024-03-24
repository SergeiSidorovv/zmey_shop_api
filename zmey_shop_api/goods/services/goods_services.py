from django.db.models.manager import BaseManager

from goods.models import Goods, CategoryGoods


def get_goods_data_for_product_cards() -> BaseManager[Goods]:
    """A function for getting goods data from database"""

    goods_data = Goods.objects.only("id", "name", "main_photo", "description", "slug")
    return goods_data


def get_goods_select_category(category_slug: str) -> BaseManager[Goods]:
    """A function for getting goods data from database by the selected category

    Keyword arguments:
    category_slug - a parameter for finding the selected product category
    """

    choice_category = CategoryGoods.objects.filter(slug=category_slug).only("id")
    if choice_category:
        category_id = choice_category.get().id
        choice_goods = Goods.objects.filter(category=category_id).only(
            "id", "name", "main_photo", "description", "slug"
        )
        return choice_goods
    return choice_category


def get_search_goods(name_product: str) -> BaseManager[Goods]:
    """A function for getting goods data from database by the desired product name

    Keyword arguments:
    name_product -- a parameter for searching for the desired product by name
    """

    search_goods = Goods.objects.filter(name__icontains=name_product).only(
        "id", "name", "main_photo", "description", "slug"
    )
    return search_goods
