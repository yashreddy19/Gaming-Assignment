from django.urls import path
from .views import GameViewSet
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="Game CRUD API",
      default_version='v1',
      description="API for managing game records, allowing CRUD operations to create, retrieve, update and delete game information.",
      contact=openapi.Contact(email="reddyyash19@gmail.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path("game/", GameViewSet.as_view({"post": "create"})),
    path(
        "game/<uuid:game_uuid>/",
        GameViewSet.as_view(
            {"patch": "update_game_details", "delete": "delete", "get": "retreive"}
        ),
    ),
    path("games/", GameViewSet.as_view({"get": "list"})),
]

#swagger UI
urlpatterns += [
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]