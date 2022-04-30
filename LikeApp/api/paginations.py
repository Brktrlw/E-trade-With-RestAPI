from rest_framework.pagination import PageNumberPagination

class CommentLikePagination(PageNumberPagination):
    page_size = 10
