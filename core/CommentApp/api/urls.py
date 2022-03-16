
from django.urls import path
from .views import ListCommentsView,CreateCommentView,DeleteCommentView,UpdateCommentView


app_name="comments"
urlpatterns = [
    path("list/<slug>",ListCommentsView.as_view(),name="url_listcomment"),
    path("create/<slug>",CreateCommentView.as_view(),name="url_createcomment"),
    path("delete/<str:unique_id>",DeleteCommentView.as_view(),name="url_deletecomment"),
    path("update/<str:unique_id>",UpdateCommentView.as_view(),name="url_updatecomment")

]
