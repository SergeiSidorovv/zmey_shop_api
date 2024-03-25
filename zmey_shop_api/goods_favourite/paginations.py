from rest_framework import pagination


class GoodsFavouritePaginations(pagination.PageNumberPagination):
    """A pagination class for viewing goods_favourite"""

    page_size = 15
