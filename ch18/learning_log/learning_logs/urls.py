"""Defines URL patterns for learning_logs."""

from django.urls import path
#from django.conf.urls import url
from . import views

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Topics Page
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path('topics/(?P<topic_id>\d+)', views.topic, name='topic'),
]

