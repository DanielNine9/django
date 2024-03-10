from django.contrib import admin
from django.urls import include, path
from .views import index
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('test/', index),
    path('api/auth/', include('users.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/', include("cart.urls"))

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

