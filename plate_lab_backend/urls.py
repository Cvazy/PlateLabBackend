from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .swagger_schema_view import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('about.urls')),
    path('', include('benefits.urls')),
    path('', include('cases.urls')),
    path('', include('comparison.urls')),
    path('api/v1/email/', include('email_sending.urls')),
    path('', include('footer.urls')),
    path('', include('gallery.urls')),
    path('', include('informations.urls')),
    path('', include('pricing.urls')),
    path(
        'api/swagger/',
        schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
