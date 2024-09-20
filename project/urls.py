from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="NP Apartments API",
        default_version="v1",
        description="An Apartment Management API for Real Estate",
        contact=openapi.Contact(email="khayratdinov.np@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path("admin/", admin.site.urls),
    path("api/v1/profiles/", include("project.apps.profiles.urls")),
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("project.apps.users.urls")),
    path("api/v1/apartments/", include("project.apps.apartments.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG_TOOLBAR:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns


admin.site.site_header = "NP Apartments Admin"
admin.site.site_title = "NP Apartments Admin Portal"
admin.site.index_title = "Welcome to NP Apartments Admin Portal"
