from django.urls import path, re_path, include
from rest_framework import routers

from . import views



urlpatterns = [
    path('', views.index, name='index'),
    re_path('match_round/(?P<match_round>\d+)/', views.match_round, name='match_round'),
    re_path('comment/', views.create_comment, name='create_comment'),
    re_path('comment/(?P<comment_id>\d+)/', views.update_comment, name='update_comment')
]