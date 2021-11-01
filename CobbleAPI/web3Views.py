"""from web3 import Web3

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from .serializers import PlayerSerializer, UserSerializer
from .models import Player
from .contractInfo import contract_address, contract_abi
from .util import *


# {"username": "greenpeppers100"}
class ReqW3Increase(APIView):
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request):
        moralis_mumbai_url = "wss://speedy-nodes-nyc.moralis.io/6249fecc67c24e15fef30131/polygon/mumbai/ws"
        web3 = Web3(Web3.WebsocketProvider(moralis_mumbai_url))

        contract = web3.eth.contract(address=contract_address, abi=contract_abi)

        username = request.data["username"]
        player = Player.objects.get(username=username)

        allowed = contract.functions.getAllowed(username).transact()
        print(allowed)"""
