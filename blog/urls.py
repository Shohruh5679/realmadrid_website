from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('trophies/', views.trophies, name='trophies'),
    path('players/', views.players, name='players'),
]

