

from django.urls import path
from .views import ListCommentLikesAPIView,CreateCommentLikeAPIView,DeleteCommentLikeAPIView

app_name="commentlikes"
urlpatterns = [
    path("commentlike/list/<unique_id>",ListCommentLikesAPIView.as_view(),name="url_listCommentLikes"),
    path("commentlike/create/",CreateCommentLikeAPIView.as_view(),name="url_createCommentLike"),
    path("commentlike/delete/<pk>",DeleteCommentLikeAPIView.as_view(),name="url_deleteCommentLike"),
]

