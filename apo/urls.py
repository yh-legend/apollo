from django.urls import path
from apo import views

urlpatterns = [
    path('', views.index, ),
]
