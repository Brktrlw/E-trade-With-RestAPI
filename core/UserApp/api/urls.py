
from django.urls import path
from .views import RegisterUserView,DeleteUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name="users"
urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='url_registeruser'),
    path("delete/",DeleteUserView.as_view(),name="url_deleteuser"),
    
    # For User Authentication (JWT)
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
