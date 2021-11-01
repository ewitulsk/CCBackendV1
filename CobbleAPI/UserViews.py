from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from .serializers import PlayerSerializer, UserSerializer
from .models import Player

from .gameSettings import *

from .util import *


# {"username": "greenpeppers100", "mcsecret": "ThisIsMySecret"}
class SetSecret(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        username = request.data['username']
        mcsecret = request.data["mcsecret"]
        print(mcsecret)
        player = Player.objects.get(username=username)
        player.mcsecret = make_password(mcsecret)

        player.save()
        return Response({"message": "Secret Changed"})


# {"username": "greenpeppers100", "from": "coal", "to": "gold (or cbbl)", "amount": 100}
class ConvertResource(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """
        blocks = 256  # 16*16 (1 chunk)

        coalPerChunk = 124
        ironPerChunk = 72
        goldPerChunk = 7.5
        diamondPerChunk = 3

        coalConversion = 1 - (coalPerChunk / blocks)  # .515625
        ironConversion = 1 - (ironPerChunk / blocks)
        goldConversion = 1 - (goldPerChunk / blocks)
        diamondConversion = 1 - (diamondPerChunk / blocks)"""

        username = request.data["username"]
        from_res = request.data["from"]
        to_res = request.data["to"]
        amount = float(request.data["amount"])
        player = Player.objects.get(username=username)

        def toCbbl(player, amount, from_res, coalConversion, ironConversion, goldConversion, diamondConversion):
            cobbleToAdd = 0
            if from_res == "coal":
                if player.coalHold < amount:
                    return player, cobbleToAdd, "Not Enough Coal"
                player.coalHold -= amount
                cobbleToAdd = amount * coalConversion

            elif from_res == "iron":
                if player.ironHold < amount:
                    return player, cobbleToAdd, "Not Enough Iron"
                player.ironHold -= amount
                cobbleToAdd = amount * ironConversion

            elif from_res == "gold":
                if player.goldHold < amount:
                    return player, cobbleToAdd, "Not Enough Gold"
                player.goldHold -= amount
                cobbleToAdd = amount * goldConversion

            elif from_res == "diamond":
                if player.diamondHold < amount:
                    return player, cobbleToAdd, "Not Enough Diamond"
                player.diamondHold -= amount
                cobbleToAdd = amount * diamondConversion

            return player, cobbleToAdd, "Success"

        def fromCbbl(player, to_res, cobbleToConvert, coalConversion, ironConversion, goldConversion, diamondConversion):
            if to_res == "coal":
                coalToGive = cobbleToConvert/coalConversion
                player.coalHold += coalToGive
            elif to_res == "iron":
                ironToGive = cobbleToConvert/ironConversion
                player.ironHold += ironToGive
            elif to_res == "gold":
                goldToGive = cobbleToConvert/goldConversion
                player.goldHold += goldToGive
            elif to_res == "diamond":
                diamondToGive = cobbleToConvert/diamondConversion
                player.diamondHold += diamondToGive
            return player

        print(request.data)

        def playerData(player, message):
            return Response({
                "message": message,
                "coalHold": str(player.coalHold),
                "ironHold": str(player.ironHold),
                "goldHold": str(player.goldHold),
                "diamondHold": str(player.diamondHold),
                "cobbleCoinHold": str(player.cobbleCoinHold)
            })

        # RES MEANS RESOURCE!!!!
        if to_res == "cbbl":
            player, cbblToAdd, message = toCbbl(player, amount, from_res, coalConversion, ironConversion, goldConversion, diamondConversion)
            player.cobbleCoinHold += cbblToAdd
            player.save()
            return playerData(player, message)

        elif from_res == "cbbl":
            if player.cobbleCoinHold < amount:
                return playerData(player, "Not Enough Cbbl")
            player = fromCbbl(player, to_res, amount, coalConversion, ironConversion, goldConversion, diamondConversion)
            player.cobbleCoinHold -= amount
            player.save()
            return playerData(player, "Success")

        elif to_res == "coal" or to_res == "iron" or to_res == "gold" or to_res == "diamond":
            player, cobbleToConvert, message = toCbbl(player, amount, from_res, coalConversion, ironConversion, goldConversion, diamondConversion)
            player = fromCbbl(player, to_res, cobbleToConvert, coalConversion, ironConversion, goldConversion, diamondConversion)
            player.save()
            return playerData(player, message)

        return playerData(player, "Incorrect Resource")