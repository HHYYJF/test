from django.urls import path
from .views import index, qq, podrobno, poisk, registration, logaut, login

urlpatterns = [
    path('', index, name='index'),
    path('qq',qq, name='qq'),
    path('poisk',poisk, name='poisk'),
    path('registration',registration, name='registration'),
    path('logaut',logaut, name='logaut'),
    path('login',login, name='login'),
    path('podrobno/<int:pk>',podrobno, name='podrobno'),


]