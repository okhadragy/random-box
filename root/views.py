from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.core import serializers
import re,requests
# Create your views here.

class Home(View):
    def get(self,request):
        boxes = Box.objects.all()
        categories = Category.objects.all()
        classification = Classification.objects.first()
        sign_up_form = Signup_Form(auto_id="signup_%s")
        login_form = Login_Form(auto_id="login_%s")
        context = {
            "boxes":boxes,
            "categories":categories,
            "classification":classification,
            "sign_up_form":sign_up_form,
            "login_form":login_form
        }
        if request.LANGUAGE_CODE == "en":
            page = "home_en.html"
        elif request.LANGUAGE_CODE == "ar":
            page = "home_ar.html"
        return render(request, page,context)

class Box_detail(View):
    def get(self,request,slug):
        box = Box.objects.get(slug=slug)
        classification = Classification.objects.first()
        sign_up_form = Signup_Form(auto_id="signup_%s")
        login_form = Login_Form(auto_id="login_%s")
        return render(request,"box_detail_ar.html",{"box":box,"classification":classification,"sign_up_form":sign_up_form,"login_form":login_form})

class Checkout(View):
    def get(self,request,slug):
        box = Box.objects.get(slug=slug)
        sign_up_form = Signup_Form(auto_id="signup_%s")
        login_form = Login_Form(auto_id="login_%s")
        return render(request,"checkout_ar.html",{"box":box,"sign_up_form":sign_up_form,"login_form":login_form})

class Pay(View):
    def get(self,request,slug):
        box = Box.objects.get(slug=slug)
        data = requests.get(url="https://api.exchangerate-api.com/v4/latest/EGP").json()
        rate = data["rates"]["USD"]
        priceUSD = round(box.price*rate, 2)
        return JsonResponse({"price":box.price,"priceUSD":priceUSD})

    def post(self,request,slug):
        player = Player.objects.get(player=request.user)
        player.balance += request.POST["price"]
        player.save_base(update_fields=["price"])
        return JsonResponse({"balance":player.balance})

class Playing(View):
    def get(self,request,slug):
        player = Player.objects.get(player=request.user)
        box = Box.objects.get(slug=slug)

        boxspin = list(BoxSpin.objects.filter(player=player,box=box))
        if boxspin:
            boxspin = BoxSpin.objects.get(player=player,box=box)
            boxspin.spin+=1
            boxspin.save_base(update_fields=["spin"])
        else:
            boxspin = BoxSpin.objects.create(player=player,box=box,spin=1)
        total_spins = len(SpinNumber.objects.all())
        player_spins = boxspin.spin
        spin_number = 0
        if total_spins>=player_spins:
            spin_number = SpinNumber.objects.get(spin_number=player_spins)
        else:
            if player_spins%total_spins == 0:
                spin_number = SpinNumber.objects.get(spin_number=20)
            else:
                spin_number = player_spins-(player_spins//total_spins)*20
                spin_number = SpinNumber.objects.get(spin_number=spin_number)

        product = Product.objects.get(spin_number=spin_number)
        prize = list(Prize.objects.filter(player=player,prize=product,box=box))
        if not prize:
            prize = Prize.objects.create(player=player,prize=product,box=box,winning_numbers = 1)
        else:
            prize = Prize.objects.get(player=player,prize=product,box=box)
            prize.winning_numbers +=1
            prize.save_base(update_fields=["winning_numbers"])
        return JsonResponse({"pk":product.pk,"message":serializers.serialize('json',[product.message,])})

class Login(View):
    def post(self,request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect(request.META['HTTP_REFERER'])

class Signup(View):
    def post(self,request):
        username = request.POST["username"]
        password = request.POST["password1"]
        form = Signup_Form(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
        else:
            print(form.errors)
        return redirect(request.META['HTTP_REFERER'])

class Signout(View):

    def get(self,request):
        logout(request)
        return redirect(request.META['HTTP_REFERER'])

class Validation(View):
    def post(self, request):
        data = request.POST
        if "sign_up_username" in data:
            username = data["sign_up_username"]
            if User.objects.filter(username=username).exists():
                return JsonResponse({"errors": "للأسف هذا الاسم مستخدم ,استخدم اسما أخر"}, status=400)
            return JsonResponse({"valid": True})
        if "sign_up_email" in data:
            regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
            email = data["sign_up_email"]
            if not (re.search(regex, str(email))):
                return JsonResponse({"errors": "هذا الإيميل غير صالح"}, status=400)
            if User.objects.filter(email=email).exists():
                return JsonResponse({"errors": "للأسف هذا الإيميل مستخدم ,استخدم إيميلا أخر"}, status=400)
            return JsonResponse({"valid": True})

        return JsonResponse({"message":"post valid data to validate it"})