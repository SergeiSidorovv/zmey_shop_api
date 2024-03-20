from rest_framework import pagination


class GoodsPaginations(pagination.PageNumberPagination):
    """A pagination class for viewing goods"""
    
    page_size = 15