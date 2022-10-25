from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path('match_round/(?P<match_round>\d+)/', views.match_round, name='match_round'),
    path('comment/', views.comment, name='comment')
]