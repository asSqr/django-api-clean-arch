from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from main.urls import urlpatterns as urls_api
from main.app.views.view_book import CreateBookAPIView

schema_view = get_schema_view(
    openapi.Info(
        title='OrderCarts API',
        default_version='1.0',
        description='API to orchestrate OrderCarts.',
        contact=openapi.Contact(email="dionvictor11@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=[
        path("", include(urls_api))
    ]
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('create/', CreateBookAPIView)
]
