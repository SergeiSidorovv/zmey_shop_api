from goods.models import Goods


def get_goods_for_product_card():
    
    goods_data = Goods.objects.only("id", "name", "main_photo", "description", "slug")
    return goods_data