from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from meteora.views import ProductViewSet, CategoryViewSet

# Define documentation
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title            = "API Documentation - Meteora",
      default_version  = 'v1',
      description      = "API Documentation - Meteora",
      terms_of_service = "https://www.google.com/policies/terms/",
      contact          = openapi.Contact(email="contact@snippets.local"),
      license          = openapi.License(name="BSD License"),
   ),
   public = True,
)

router = routers.DefaultRouter()

router.register('products',   ProductViewSet,  basename = 'Products')
router.register('categories', CategoryViewSet, basename = 'Categories')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout = 0), name = 'schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
