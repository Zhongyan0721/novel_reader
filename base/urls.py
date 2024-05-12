from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('novel/<str:id>/', views.novel, name = "novel")
]