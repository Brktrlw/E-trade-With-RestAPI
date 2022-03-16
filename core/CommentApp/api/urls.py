
from django.urls import path
from .views import ListCommentsView,CreateCommentView


app_name="comments"
urlpatterns = [
    path("list/<slug>",ListCommentsView.as_view(),name="url_listcomment"),
    path("create/<slug>",CreateCommentView.as_view(),name="url_createcomment")

]
