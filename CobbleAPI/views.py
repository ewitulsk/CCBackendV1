from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from .serializers import PlayerSerializer, UserSerializer
from .models import Player

from .util import *


# Create your views here.
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by('username')
    serializer_class = PlayerSerializer
    permission_classes = (AllowAny, )


# {"username": "greenpeppers100"}
class GetCBBLHold(APIView):
    def post(self, request):
        username = request.data["username"]
        player = Player.objects.get(username=username)
        return Response({"message": player.cobbleCoinHold})


# {"username": "green"}
class GetUserResource(APIView):
    def post(self, request):
        username = request.data["username"]

        try:
            player = Player.objects.get(username=username)
        except:
            return Response({"message": "Error, username does not exist"})

        res = {
            "message": "Success",
            "coalHold": str(player.coalHold),
            "ironHold": str(player.ironHold),
            "goldHold": str(player.goldHold),
            "diamondHold": str(player.diamondHold),
            "cobbleCoinHold": str(player.cobbleCoinHold)
        }

        return Response(res)


# {"username": "green"}
class GetUserSigns(APIView):
    def post(self, request):
        username = request.data["username"]

        try:
            player = Player.objects.get(username=username)
        except:
            return Response({"message": "Error, username does not exist"})

        res = {
            "message": "Success",
            "coalSigns": str(player.coalSigns),
            "allowedCoalSigns": str(player.allowedCoalSigns),
            "ironSigns": str(player.ironSigns),
            "allowedIronSigns": str(player.allowedIronSigns),
            "goldSigns": str(player.goldSigns),
            "allowedGoldSigns": str(player.allowedGoldSigns),
            "diamondSigns": str(player.diamondSigns),
            "allowedDiamondSigns": str(player.allowedDiamondSigns),
        }

        return Response(res)


# {"mcusername": "greenpeppers100"}
class GetCobbleBalanceMC(APIView):
    def post(self, request):
        mcusername = request.data["mcusername"]
        player = Player.objects.get(mcusername=mcusername)
        return Response({"amount": player.cobbleCoinHold})


class GetCobbleBalanceUser(APIView):
    def post(self, request):
        username = request.data["username"]
        user = Player.objects.get(username=username)
        return Response({"amount": user.cobbleCoinHold})


# {"senderMcusername": "greenpeppers100", "recieverMcusername": "testUser", "amount": 100}
class TransferCobble(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request):
        senderMC = request.data["senderMcusername"]
        recieverMC = request.data["recieverMcusername"]
        amount = request.data['amount']

        sender = Player.objects.get(mcusername=senderMC)
        reciever = Player.objects.get(mcusername=recieverMC)

        # send_cobble returns true on success, returns false on fail
        # If send cobble is false, return error
        if not send_cobble(amount, sender, reciever):
            return Response({"message": "Error, Insufficient funds"})

        return Response({"message": sender.cobbleCoinHold})


class HelloView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': 'Hello World!'}
        return Response(content)


class Echo(APIView):
    permission_classes = (IsAuthenticated, )
    def post(self, request, *args, **kwargs):
        print(request.data)
        return Response(request.data)


class AuthView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        """
        player = Player.objects.get(username=user.username)
        if not player.validated:
            return Response({
                'please validate minecraft username'
            })"""
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.username
        })