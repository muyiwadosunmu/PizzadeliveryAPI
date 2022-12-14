
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view= get_schema_view(
   openapi.Info(
      title="Pizza_delivery_API",
      default_version='v1',
      description="A REST API built with django rest framework for pizza_delivery",
      contact=openapi.Contact(email="oluwamuyiwadosunmu@gmail.com"),
      license=openapi.License(name="ΔΔuyiw@.dev"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('orders/', include('orders.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('swagger<format>.json|.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
