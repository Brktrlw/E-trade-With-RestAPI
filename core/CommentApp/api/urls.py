
from django.urls import path
from .views import ListCommentsAPIView,CreateCommentAPIView,DeleteCommentAPIView,UpdateCommentAPIView

app_name="comments"
urlpatterns = [
    path("list/<slug>",ListCommentsAPIView.as_view(),name="url_listcomment"),
    path("create/<slug>",CreateCommentAPIView.as_view(),name="url_createcomment"),
    path("delete/<str:unique_id>",DeleteCommentAPIView.as_view(),name="url_deletecomment"),
    path("update/<str:unique_id>",UpdateCommentAPIView.as_view(),name="url_updatecomment")

]
