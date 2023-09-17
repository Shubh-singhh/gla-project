from . import views
from django.urls import path
urlpatterns = [
    # path('',views.login1),
    path('',views.index,name="index"),
    # path('saveEnquiry/',views.saveEnquiry,name="saveEnquiry"),
    path('login1/',views.login1,name="login1"),
    path('community/',views.community,name="community"),
    path('community/Event/',views.Event,name="Event"),
    path('community/leaderboard/Event/',views.Event,name="Event"),
    path('community/Profile/Event/',views.Event,name="Event"),

    path('community/Event/Profile/',views.Profile,name="Profile"),
    path('community/Profile/',views.Profile,name="Profile"),
    path('community/leaderboard/',views.leaderboard,name="leaderboard"),
    path('community/Event/leaderboard/',views.leaderboard,name="leaderboard"),
    path('community/Event/Profile/leaderboard/',views.leaderboard,name="leaderboard"),
    path('community/Profile/leaderboard/',views.leaderboard,name="leaderboard"),
    path('community/Complaim/leaderboard/',views.leaderboard,name="leaderboard"),
    path('community/Profile/Event/leaderboard/',views.leaderboard,name="leaderboard"),

    path('community/Wallet',views.Wallet,name="Wallet"),
    path('community/leaderboard/Wallet',views.Wallet,name="Wallet"),
    path('community/Event/Wallet',views.Wallet,name="Wallet"),
    path('community/Event/leaderboard/Wallet',views.Wallet,name="Wallet"),
    path('community/Event/Profile/Event/Wallet',views.Wallet,name="Wallet"),
    path('community/Event/Profile/Wallet',views.Wallet,name="Wallet"),




    path('community/Event/Complain/',views.Complain,name="Complain"),
    path('community/Event/Profile/Complain',views.Complain,name="Complain"),
    path('community/Complain',views.Complain,name="Complain"),
    path('community/Event/leaderboard/Complain',views.Complain,name="Complain"),


    path('dashboard/',views.dashboard,name="dashboard"),
    path('Signup/',views.Signup,name="Signup"),
    path('Invalid/',views.Invalid,name="Invalid"),
    path('logout/',views.logout,name="logout")
]
