from django.contrib import admin
from django.urls import path,include
from Account.views import UserLogin, UserProfile, UserRegister
urlpatterns = [
    path('register/',UserRegister.as_view(),name='register'),
    path('login/',UserLogin.as_view(),name='login'),
    path('profile/',UserProfile.as_view(),name='profile'),

    
    

]
