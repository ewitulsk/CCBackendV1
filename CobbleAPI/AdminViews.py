from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from .serializers import PlayerSerializer, UserSerializer, ExchangeSerializer
from .models import Player, Exchange

from .gameSettings import *
from .util import *


"""
Every view here MUST haveIsAdminUser
"""


class ExchangeViewSet(viewsets.ModelViewSet):
    queryset = Exchange.objects.all().order_by('name')
    serializer_class = ExchangeSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            exchange = Exchange.objects.get(name=request.data['name'])
            exchange.coalSignOwner = request.data['registeree']
            exchange.ironSignOwner = request.data['registeree']
            exchange.goldSignOwner = request.data['registeree']
            exchange.diamondSignOwner = request.data['registeree']
            exchange.save()
            return Response({'message': 'success'})
        return Response({'message': 'error'})

    def put(self, request):
        name = request.data['name']
        exchange_object = Exchange.objects.get(name=name)
        serializer = ExchangeSerializer(exchange_object, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'success'})
        return Response({'message': 'error'})


"""
GIVE SIGN IS BROKEN UNTIL YOU FIX IT!!!
# send {'exchange': 'GreenEx', 'resource':'coal', 'mcusername': 'greenpeppers100', 'receiver': 'thepiggygun'}
class GiveSign(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request):
        mcusername = request.data['mcusername']
        exchangeName = request.data['exchange']
        receiverName = request.data['receiver']
        resource = request.data['resource']

        player = Player.objects.get(mcusername=mcusername)
        receiver = Player.objects.get(mcusername=receiverName)
        exchange = Exchange.objects.get(name=exchangeName)

        print(f"Registeree: {exchange.registeree}")
        print(f"MCUsername: {player.mcusername}")

        if exchange.registeree == player.mcusername:
            if resource == "coal":
                exchange.coalSignOwner = receiver.mcusername
            elif resource == "iron":
                exchange.ironSignOwner = receiver.mcusername
            elif resource == "gold":
                exchange.goldSignOwner = receiver.mcusername
            elif resource == "diamond":
                exchange.diamondSignOwner = receiver.mcusername
            else:
                return Response({'message': 'Error, invalid resource'})
        else:
            return Response({'message': 'Error, you dont own that exchange'})
        player.save()
        exchange.save()
        return Response({'message': f'{resource} sign assigned to {receiverName}'})
"""

# YOU LEFT OFF HERE, YOU GOTTA MAKE IT SO IT JUST CHECKS IF THE EXCHANGE SIGN IS SET AND IF THE OWNER IS THE PLAYER TRYING TO PLACE THE SIGN

# {'mcusername': 'green', 'exchangeName': 'ThisIsExchangeName', 'resource': 'coal', 'locationX' 100, 'locationY': -105, 'locationZ': 75}
class PlaceSign(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    def post(self, request):
        resource = request.data['resource']
        mcusername = request.data['mcusername']
        exchangeName = request.data['exchangeName']

        locationX = int(request.data['locationX'])
        locationY = int(request.data['locationY'])
        locationZ = int(request.data['locationZ'])
        locationWorld = request.data['locationWorld']

        try:
            exchange = Exchange.objects.get(name=exchangeName)
        except:
            return Response({"message": "Exchange does not exist."})

        player = Player.objects.get(mcusername=mcusername)

        if resource == "coal" and player.mcusername == exchange.coalSignOwner and not exchange.coalSignSet:
            exchange.coalSignLocationWorld = locationWorld
            exchange.coalSignLocationX = locationX
            exchange.coalSignLocationY = locationY
            exchange.coalSignLocationZ = locationZ
            exchange.coalSignSet = True
            rate = coalConversion

        elif resource == "iron" and player.mcusername == exchange.ironSignOwner and not exchange.ironSignSet:
            exchange.ironSignLocationWorld = locationWorld
            exchange.ironSignLocationX = locationX
            exchange.ironSignLocationY = locationY
            exchange.ironSignLocationZ = locationZ
            exchange.ironSignSet = True
            rate = ironConversion

        elif resource == "gold" and player.mcusername == exchange.goldSignOwner and not exchange.goldSignSet:
            exchange.goldSignLocationWorld = locationWorld
            exchange.goldSignLocationX = locationX
            exchange.goldSignLocationY = locationY
            exchange.goldSignLocationZ = locationZ
            exchange.goldSignSet = True
            rate = goldConversion

        elif resource == "diamond" and player.mcusername == exchange.diamondSignOwner and not exchange.diamondSignSet:
            exchange.diamondSignLocationWorld = locationWorld
            exchange.diamondSignLocationX = locationX
            exchange.diamondSignLocationY = locationY
            exchange.diamondSignLocationZ = locationZ
            exchange.diamondSignSet = True
            rate = diamondConversion
        else:
            return Response({'message': f"Error, you do not own the {resource} sign for {exchangeName}"})

        player.save()
        exchange.save()
        print("Placed Sign")
        return Response({'message': "success"})


# {'mcusername': 'green', 'exchangeName': 'ThisIsExchangeName', 'resource': 'coal'}
class RemoveSign(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    def post(self, request):
        resource = request.data['resource']
        mcusername = request.data['mcusername']
        exchangeName = request.data['exchangeName']

        try:
            exchange = Exchange.objects.get(name=exchangeName)
        except:
            return Response({"message": "Exchange Does Not Exist"})

        player = Player.objects.get(mcusername=mcusername)

        if resource == "coal" and exchange.coalSignSet and player.mcusername == exchange.coalSignOwner:
            exchange.coalSignLocationX = 0
            exchange.coalSignLocationY = 0
            exchange.coalSignLocationZ = 0
            exchange.coalSignSet = False

        elif resource == "iron" and exchange.ironSignSet and player.mcusername == exchange.ironSignOwner:
            exchange.ironSignLocationX = 0
            exchange.ironSignLocationY = 0
            exchange.ironSignLocationZ = 0
            exchange.ironSignSet = False

        elif resource == "gold" and exchange.goldSignSet and player.mcusername == exchange.goldSignOwner:
            exchange.goldSignLocationX = 0
            exchange.goldSignLocationY = 0
            exchange.goldSignLocationZ = 0
            exchange.goldSignSet = False

        elif resource == "diamond" and exchange.diamondSignSet and player.mcusername == exchange.diamondSignOwner:
            exchange.diamondSignLocationX = 0
            exchange.diamondSignLocationY = 0
            exchange.diamondSignLocationZ = 0
            exchange.diamondSignSet = False
        else:
            return Response({'message': f"Error, you do not own the {resource} sign for {exchangeName} or the sign is not set"})

        player.save()
        exchange.save()
        return Response({"message": "success"})

"""
TRANSFER SIGN IS BROKEN UNTILL YOU FIX IT!!!!
# {'sender': 'green', 'receiver':'thepiggygun', 'exchangeName': 'GreenExchange1', 'resource': 'coal'}
class TransferSign(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    def post(self, request):
        resource = request.data['resource']
        sender = request.data['sender']
        receiver = request.data['receiver']
        exchangeName = request.data['exchangeName']

        exchange = Exchange.objects.get(name=exchangeName)
        sender = Player.objects.get(mcusername=sender)
        receiver = Player.objects.get(mcusername=receiver)

        if resource == "coal" and sender.mcusername == exchange.coalSignOwner:
            if exchange.coalSignSet:
                return Response({'message': 'you can not transfer a placed sign'})
            exchange.coalSignOwner = receiver.mcusername
            sender.coalSigns -= 1
            receiver.coalSigns += 1
            senderAmount = sender.coalSigns
            receiverAmount = receiver.coalSigns

        elif resource == "iron" and sender.mcusername == exchange.ironSignOwner:
            if exchange.ironSignSet:
                return Response({'message': 'you can not transfer a placed sign'})
            exchange.ironSignOwner = receiver.mcusername
            sender.ironSigns -= 1
            receiver.ironSigns += 1
            senderAmount = sender.ironSigns
            receiverAmount = receiver.ironSigns

        elif resource == "gold" and sender.mcusername == exchange.goldSignOwner:
            if exchange.goldSignSet:
                return Response({'message': 'you can not transfer a placed sign'})
            exchange.goldSignOwner = receiver.mcusername
            sender.goldSigns -= 1
            receiver.goldSigns += 1
            senderAmount = sender.goldSigns
            receiverAmount = receiver.goldSigns

        elif resource == "diamond" and sender.mcusername == exchange.diamondSignOwner:
            if exchange.diamondSignSet:
                return Response({'message': 'you can not transfer a placed sign'})
            exchange.diamondSignOwner = receiver.mcusername
            sender.diamondSigns -= 1
            receiver.diamondSigns += 1
            senderAmount = sender.diamondSigns
            receiverAmount = receiver.diamondSigns
        else:
            return Response({'message': f"Error, you do not own the {resource} sign for {exchangeName} or the sign is not set"})

        sender.save()
        receiver.save()
        exchange.save()
        return Response({'senderAmount': senderAmount, 'receiverAmount': receiverAmount})
"""

"""
BROKEN!!!
# {'mcusername': 'greenpeppers100', 'resource': 'coal'}
class GetSignBal(APIView):
    permission_classes = (IsAdminUser, IsAuthenticated)

    def post(self, request):
        mcusername = request.data['mcusername']
        resource = request.data['resource']
        player = Player.objects.get(mcusername=mcusername)
        if resource == "coal":
            return Response({'message': player.coalSigns})
        elif resource == "iron":
            return Response({'message': player.ironSigns})
        elif resource == "gold":
            return Response({'message': player.goldSigns})
        elif resource == "diamond":
            return Response({'message': player.diamondSigns})
        return Response({'message': 'Invalid Resource'})
"""

# send {'username': 'greenpeppers100', 'as':'add', 'amount':100}
# send {'username': 'greenpeppers100', 'as':'sub', 'amount':100}
class AddSubCBBL(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request):
        username = request.data["username"]
        addSub = request.data["as"]
        amount = float(request.data["amount"])

        players = Player.objects.get(username=username)
        if addSub == "add":
            players.cobbleCoinHold += amount
        elif addSub == "sub":
            players.cobbleCoinHold -= amount
        players.save()
        return Response({"message": players.cobbleCoinHold})


# send {'mcusername': 'greenpeppers100', 'resource': 'coal', 'amount': 64}
class IncreaseResource(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request):
        playermcname = request.data['mcusername']
        resource = request.data['resource']
        amount = int(request.data['amount'])

        players = Player.objects.get(mcusername=playermcname)
        if resource == "coal":
            players.coalHold += amount
            current_holding = players.coalHold
        elif resource == "iron":
            players.ironHold += amount
            current_holding = players.ironHold
        elif resource == "gold":
            players.goldHold += amount
            current_holding = players.goldHold
        elif resource == "diamond":
            players.diamondHold += amount
            current_holding = players.diamondHold
        players.save()
        return Response({"message": current_holding})


# send {'mcusername': 'greenpeppers100'}
class ToValidateView(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request):
        playermcname = request.data['mcusername']
        players = Player.objects.filter(validated=False)
        for player in players:
            if player.mcusername == playermcname:
                return Response({'mcusername': playermcname, 'username': player.username, 'message': 'awaiting'})
        return Response({'message': 'not awaiting'})


# to send {'username': 'BackendUsername'}
# This is a shitty hack, fix as soon as you know how!
class ValidateUser(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request):
        mcusername = request.data['mcusername']
        players = Player.objects.filter(validated=False)
        for player in players:
            if player.mcusername == mcusername:
                player.validated = True
                player.save()
                # Successfully validated user
                return Response({'message': 'validated'})
        # Either user doesn't exist, or is already validated.
        return Response({'message': 'validation error'})


# to send {'username': 'BackendUsername'}
# This is a shitty hack, fix as soon as you know how!
class DoNotValidateUser(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request):
        mcusername = request.data['mcusername']
        players = Player.objects.filter(validated=False)
        for player in players:
            if player.mcusername == mcusername:
                player.mcusername = ""
                player.save()
                # Successfully unregistered mcusername
                return Response({'message': 'success'})
        # Either user doesn't exist, or is already validated.
        return Response({'message': 'error'})


class CheckSecret(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request):
        secret = request.data['mcsecret']
        mcusername = request.data['mcusername']
        players = Player.objects.all()
        for player in players:
            if player.mcusername == mcusername:
                hashed_secrete = player.mcsecret
                if check_password(secret, hashed_secrete):
                    return Response({'message': 'correct'})
                else:
                    return Response({'message': 'incorrect'})
        # MCUsername is not associated with an account
        return Response({'message': 'error'})


"""
class PurchaseExchange(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request):"""


# {"username": "greenpeppers100", "amount": 100}
class RemoveCBBL(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request):
        username = request.data["username"]
        amount = request.data["amount"]
        player = Player.objects.get(username=username)
        player.cobbleCoinHold -= amount
        player.save()
        return Response({"amount": player.cobbleCoinHold})