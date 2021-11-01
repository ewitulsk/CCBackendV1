from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Player, Exchange
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password


class ExchangeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exchange
        fields = ('name', 'exFee', 'registeree', 'coalSignOwner', 'ironSignOwner', 'goldSignOwner', 'diamondSignOwner', 'coalSignFee', 'ironSignFee', 'goldSignFee', 'diamondSignFee', 'coalSignSet', 'coalSignLocationWorld','coalSignLocationX', 'coalSignLocationY', 'coalSignLocationZ', 'ironSignSet', 'ironSignLocationWorld','ironSignLocationX', 'ironSignLocationY', 'ironSignLocationZ', 'goldSignSet', 'goldSignLocationWorld','goldSignLocationX', 'goldSignLocationY', 'goldSignLocationZ', 'diamondSignSet', 'diamondSignLocationWorld','diamondSignLocationX', 'diamondSignLocationY', 'diamondSignLocationZ')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        return user


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Player
        fields = ('user', 'mcusername', 'mcsecret')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        mcsecret = validated_data.pop('mcsecret')
        user = User.objects.create(**user_data)
        user.set_password(password)
        user.save()
        token = Token.objects.create(user=user)
        token.save()
        player = Player.objects.create(username=user.username, validated=False, user=user, **validated_data)
        player.mcsecret = make_password(mcsecret)
        player.save()
        return player
