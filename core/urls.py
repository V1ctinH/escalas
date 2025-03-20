from django.urls import path
from django.shortcuts import render

from core.views import escalas

urlpatterns = [
    path('escalas/', escalas, name='escalas'),
]
