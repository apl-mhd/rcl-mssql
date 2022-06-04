from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/product/', include('products.urls')),
    path('api/customer/', include('users.urls')),
    path('api/', include('orders.urls')),
    path('api/user/', include('user_app.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
