from django.urls import path, re_path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('comment', views.CommentView)

urlpatterns = [
    path('', views.index, name='index'),
    re_path('match_round/(?P<match_round>\d+)/', views.match_round, name='match_round'),
    path('', include(router.urls)),
    path('edit_match', views.edit_match_view, name='edit_match')
]
