from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calculator/', views.calculator, name='calculator'),
    path('registration/', views.registration, name='registration'),
    path('programmer-day/', views.programmer_day, name='programmer_day'),
]
