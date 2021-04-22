"""Defines URL patterns for pizzas."""

from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    path('pizzas/', views.pizzas, name='pizzas'),
    path('pizzas/(?P<pizza_id>\d+)/', views.pizza, name='pizza'),
]