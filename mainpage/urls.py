from django.urls import path
from . import views

urlpatterns = [
    path('', views.HeroView.as_view(), name='home'),


]
