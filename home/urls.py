from django.urls import path,include
from .views import *
urlpatterns = [
    path('',home, name='home'),
    path('home',home_page, name='home_page'),
    path('fruits_list', fruits_list, name='fruits_list')
]

