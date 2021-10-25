from rest_framework import serializers
from .models import Game, Party, Message, CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'steam_user', 'discord_user']


class GameSerializer(serializers.HyperlinkedModelSerializer):
    added_by = UserSerializer()

    class Meta:
        model = Game
        fields = ('name', 'added_by', 'created_date')


class PartySerializer(serializers.HyperlinkedModelSerializer):
    added_by = UserSerializer()

    class Meta:
        model = Party
        fields = ('name', 'added_by', 'created_date', 'game_id')


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    added_by = UserSerializer()

    class Meta:
        model = Message
        fields = ('content', 'added_by', 'created_date', 'party_id')
