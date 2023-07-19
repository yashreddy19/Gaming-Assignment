from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .serializers import GameSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
)
from rest_framework.request import Request
from .models import Game
from uuid import UUID
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class GameViewSet(ViewSet, ListAPIView):
    serializer_class = GameSerializer
    PageNumberPagination.page_size_query_param = "page_size"
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Game.objects.all().order_by("-created_at")

    def create(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=HTTP_400_BAD_REQUEST, data=serializer.errors)
        serializer.save()
        return Response(status=HTTP_201_CREATED, data=serializer.validated_data)

    def update_game_details(self, request: Request, game_uuid: UUID) -> Response:
        game_instance = Game.objects.filter(uuid=game_uuid).first()
        if not game_instance:
            return Response(status=HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(
            data=request.data, partial=True, instance=game_instance
        )
        if not serializer.is_valid():
            Response(status=HTTP_400_BAD_REQUEST, data=serializer.errors)
        serializer.save()
        return Response(status=HTTP_200_OK, data=serializer.data)

    def delete(self, request: Request, game_uuid: UUID) -> Response:
        game_instance: Game = Game.objects.filter(uuid=game_uuid).first()
        if not game_instance:
            return Response(status=HTTP_404_NOT_FOUND)
        game_instance.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    def retreive(self, request: Request, game_uuid: UUID) -> Response:
        game_instance: Game = Game.objects.filter(uuid=game_uuid).first()
        if not game_instance:
            return Response(status=HTTP_404_NOT_FOUND)
        serializered_data = self.get_serializer(instance=game_instance).data
        return Response(status=HTTP_200_OK, data=serializered_data)
