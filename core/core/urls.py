
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/products/",include("ProductsApp.api.urls",namespace="products")),
    path("api/carts/",include("CartApp.api.urls",namespace="carts")),
    path("api/comments/", include("CommentApp.api.urls", namespace="comments")),
    path("api/user/",include("UserApp.api.urls",namespace="users")),
    path("api/favorites/",include("FavoritesApp.api.urls",namespace="favorites")),
    path("api/orders/",include("OrderApp.api.urls",namespace="orders"))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)