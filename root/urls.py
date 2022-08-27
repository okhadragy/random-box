from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    path("",Home.as_view(),name="home"),
    path("boxes/<slug:slug>/",Box_detail.as_view(),name="Box_detail"),
    path("checkout/<slug:slug>/",Checkout.as_view(),name="checkout"),
    path("pay/<slug:slug>/",csrf_exempt(Pay.as_view()),name="pay"),
    path("playing/<slug:slug>/",Playing.as_view(),name="playing"),
    path("login/",Login.as_view(),name="login"),
    path("signup/",Signup.as_view(),name="signup"),
    path("signout/",Signout.as_view(),name="signout"),
    path("validate/",csrf_exempt(Validation.as_view()),name="validate"),
] 
