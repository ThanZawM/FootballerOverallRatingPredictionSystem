from django.urls import path
from . import views

urlpatterns = [
    path('', views.football, name='football'),
    path('about/', views.about, name='about'),
    path('rmse/', views.rmse, name='rmse'),
]