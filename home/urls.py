

from django.urls import path
from home import views

urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('search/', views.search,name='search'),
    path('singup/', views.singup,name='singup'),
    path('loginl/', views.loginl,name='loginl'),
    path('logoutl/', views.logoutl,name='logoutl'),
]
