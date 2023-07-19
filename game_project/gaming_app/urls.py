from django.urls import path
from .views import GameViewSet

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
