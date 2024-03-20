from goods.models import Goods


def get_goods_data_for_product_cards():
    """A function for getting goods data for displaying product card"""

    goods_data = Goods.objects.only("id", "name", "main_photo", "description", "slug")
    return goods_data
