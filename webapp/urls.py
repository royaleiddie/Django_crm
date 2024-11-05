from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('register', views.register, name='register'),
    path('mylogin', views.myLogin, name='mylogin'),
    path('userlogout', views.userLogout, name='userlogout'),
    path('dashboard', views.dashboard, name='dashboard'),
]


