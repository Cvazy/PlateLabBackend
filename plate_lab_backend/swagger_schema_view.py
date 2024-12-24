from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from decouple import config
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

schema_view = get_schema_view(
   openapi.Info(
      title="PlateLab API",
      default_version='v1',
      description="API documentation for all models",
      contact=openapi.Contact(email=config('EMAIL')),
   ),
   public=True,
   authentication_classes=[SessionAuthentication],
   permission_classes=[IsAuthenticated],
)
