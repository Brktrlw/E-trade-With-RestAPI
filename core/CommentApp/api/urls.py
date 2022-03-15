
from django.urls import path
from .views import ListCommentsView


app_name="comments"
urlpatterns = [
    path("list/<slug>",ListCommentsView.as_view(),name="url_listcomment")
]
