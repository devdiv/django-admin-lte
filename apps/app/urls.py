# -*- encoding: utf-8 -*-
from django.urls import path, re_path
from apps.app import views

urlpatterns = [

    # The app page
    path('', views.index, name='app'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
