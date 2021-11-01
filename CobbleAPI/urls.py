from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from . import AdminViews
from . import UserViews
from . import web3Views

router = routers.DefaultRouter()
# api/router/...
router.register(r'players', views.PlayerViewSet)
router.register(r'exchanges', AdminViews.ExchangeViewSet)

# Wire up API using automatic URL routing.
# We also include login URLs for the browsable API
urlpatterns = [
    path('router/', include(router.urls)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('hello/', views.HelloView.as_view(), name='hello'),
    # path('account/register/', views.CreateUserView.as_view(), name='register'),
    path('api-token-auth/', views.AuthView.as_view(), name='api_token_auth'),
    path('echo/', views.Echo.as_view(), name='echo'),

    # {"username": "greenpeppers100", "mcsecret":"ThisIsMySecret"}
    path('setSecret/', UserViews.SetSecret.as_view(), name='setSecret'),

    # {"username": "green"}
    path('getUserResource/', views.GetUserResource.as_view(), name="getUserResource"),
    path('getUserSigns/', views.GetUserSigns.as_view(), name='getUserSigns'),

    path('getCBBLBalanceMC/', views.GetCobbleBalanceMC.as_view(), name='getCobbleBalanceMC'),
    path('getCBBLBalanceUser/', views.GetCobbleBalanceUser.as_view(), name='getCobbleBalanceUser'),
    path('transferCobble/', views.TransferCobble.as_view(), name='transferCobble'),
    path('removeCobble/', AdminViews.RemoveCBBL.as_view(), name='removeCobble'),

    # These are Admin specific views
    path('validate/', AdminViews.ValidateUser.as_view(), name='validate'),
    path('doNotValidate/', AdminViews.DoNotValidateUser.as_view(), name='doNotValidate'),
    path('toValidate/', AdminViews.ToValidateView.as_view(), name='toValidate'),
    path('checkSecret/', AdminViews.CheckSecret.as_view(), name='checkSecret'),
    path('increaseResource/', AdminViews.IncreaseResource.as_view(), name='increaseResource'),

    # send {'username': 'greenpeppers100', 'as':'add', 'amount':100}
    # send {'username': 'greenpeppers100', 'as':'sub', 'amount':100}
    path('addSubCBBL/', AdminViews.AddSubCBBL.as_view(), name='addSubCBBL'),

    # Give Sign Is Broken Until You Fix It!!!!
    #path('giveSign/', AdminViews.GiveSign.as_view(), name='giveSign'),

    # {'mcusername': 'green', 'exchangeName': 'ThisIsExchangeName', 'resource': 'coal', 'locationX' 100, 'locationY': -105, 'locationZ': 75}
    path('placeSign/', AdminViews.PlaceSign.as_view(), name='placeSign'),

    path('removeSign/', AdminViews.RemoveSign.as_view(), name='removeSign'),
    # TRANSFER SIGN IS BROKEN!!!
    # path('transferSign/', AdminViews.TransferSign.as_view(), name='transferSign'),
    # Broken!!!
    # path('getSignBal/', AdminViews.GetSignBal.as_view(), name='getSignBal'),


    # These are Web3 specific views
    # path('reqIncrease/', web3Views.ReqW3Increase.as_view(), name='reqIncrease'),

    # These are User specific views
    # {"username": "greenpeppers100", "from": "coal", "to": "gold (or cbbl)", "amount": 100}
    path('convertResource/', UserViews.ConvertResource.as_view(), name='convertResource'),
]