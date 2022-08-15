from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index1, name='index1'),
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('login/', views.login, name='login'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('login/Lost/', views.Lost, name='Lost'),
    path('login/Find/', views.Find, name='Find'),
    path('login/Find/Search/', views.Search, name='Search'),
    #path('find/', views.dect, name='dect'),
]

