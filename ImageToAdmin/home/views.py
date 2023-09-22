from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from . models import Note
# from . models import Records
# Create your views here.
def dashboard(request):
    user = request.user 
    return render(request,"dashboard.html")

def Invalid(request):
    return render(request,"Invalid.html")

# @login_required(login_url="login1")
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
        myuser = User.objects.create_user(uname = uname,fname = fname,lname = lname)
        myuser.save()
        messages.success(request,"Successfully Login!!")
        return redirect("dashboard")

    return render(request,"Signup.html")
    
# @login_required(login_url="login1")
def logout(request):
    logout(request)
    return render(request,"login1.html")

def index(request):
    if request.method == "POST":
        userr = request.POST.get("userr")
        uemail = request.POST.get("uemail")
        ucomment = request.POST.get("ucomment")
        new_note = Note.objects.create(userr = userr,uemail = uemail,ucomment = ucomment)
        new_note.save()
        return redirect("index")
    return render(request,"index.html")


@login_required(login_url="login1")
def community(request):
    return render(request,"community.html")


@login_required(login_url="login1")
def Event(request):
    return render(request,"Event.html")

@login_required(login_url="login1")
def Profile(request):
    user = request.user
    notes = Note.objects.all()
    # parameters = {
    #     "user":user,
    #     "notes":notes
    # }
    return render(request,"Profile.html")

@login_required(login_url="login1")
def Complain(request):
    # demoProfile = Records.objects.raw('SELECT id, name, image FROM demo_demoprofile')
    # args = {'profile':demoProfile}
    return render(request,"complain.html")

@login_required(login_url="login1")
def leaderboard(request):
    return render(request,"Leaderboard.html")

@login_required(login_url="login1")
def Wallet(request):
    return render(request,"Wallet.html")

@login_required(login_url="login1")
def YourPost(request):
    return render(request,"YourPost.html")

@login_required(login_url="login1")
def CreatePost(request):
    return render(request,"CreatePost.html")