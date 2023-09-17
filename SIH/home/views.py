from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from home.models import Feedback 
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def dashboard(request):
    user = request.user 
    return render(request,"dashboard.html")

def Invalid(request):
    return render(request,"Invalid.html")

def login1(request):
    if request.method == "POST":
        username = request.POST.get("username")
        userpass = request.POST.get("userpass")
        re_enter = request.POST.get("re_enter")
        user = authenticate(request,username = username,password = userpass)
        if userpass == re_enter:
            if user is not None:
                login(request, user)
                return redirect("community")
            else:
                return redirect("login1")
        else:
            return redirect("login1")
    return render(request,"login1.html")

# def saveEnquiry(request):
#     if request.method == "POST":
#         ufeedback = request.POST.get('ufeedback')
#         uemail = request.POST.get('uemail')
#         ucomment = request.POST.get('ucomment')
#         fb = Feedback(title=ufeedback,email=uemail,description=ucomment)
#         fb.save()
#     return render(request,"index.html")

def Signup(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        upass = request.POST.get("upass")
        # if upass1!=upass2:
        #     return HttpResponse("You entered wrong pass")
        # else:
        #     myuser = User.objects.create_user(uname,fname,lname)
        #     myuser.fname = fname
        #     myuser.lname = lname myuser.save()
        myuser = User.objects.create_user(uname,fname,lname)
        myuser.fname = fname
        myuser.lname = lname
        myuser.save()
        messages.success(request,"Successfully Login!!")
        return redirect("dashboard")

    return render(request,"Signup.html")

def logout(request):
    logout(request)
    return render(request,"login1.html")

def index(request):
    # if request.method == "POST":
    return render(request,"index.html")

@login_required()
def community(request):
    return render(request,"community.html")
@login_required()
def Event(request):
    return render(request,"Event.html")
@login_required()
def Profile(request):
    return render(request,"Profile.html")
@login_required()
def Complain(request):
    return render(request,"complain.html")

def leaderboard(request):
    return render(request,"Leaderboard.html")

def Wallet(request):
    return render(request,"Wallet.html")