
from django.urls import path
from .views import RegisterView


app_name="users"
urlpatterns = [
    path('register/', RegisterView.as_view(), name='url_register'),
]
