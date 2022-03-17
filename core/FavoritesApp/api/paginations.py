from rest_framework.pagination import PageNumberPagination

class FavoritePagination(PageNumberPagination):
    page_size = 10