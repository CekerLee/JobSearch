# -*- coding: utf-8 -*-
from django.urls import path

from app import views

__author__ = 'cekerlee'

urlpatterns = [
    path('', views.index, name="index"),
    path('result/', views.result, name="result"),
]
