
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/products/",include("ProductsApp.api.urls",namespace="products")),
    path("api/carts/",include("CartApp.api.urls",namespace="carts"))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)