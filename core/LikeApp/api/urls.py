

from django.urls import path
from .views import ListCommentLikes

app_name="commentlikes"
urlpatterns = [
    path("comment/<comment_id>",ListCommentLikes.as_view(),name="url_listCommentLikes")


]

