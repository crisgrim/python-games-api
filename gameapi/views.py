from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import GameSerializer, PartySerializer, MessageSerializer, UserSerializer
from .models import Game, Party, Message, CustomUser


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('name')
    serializer_class = GameSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all().order_by('name')
    serializer_class = PartySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['game_id']


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().order_by('created_date')
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['party_id']


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_fields = ['username']
