from django.urls import path
from apo import views

urlpatterns = [
    path('', views.index, ),
    path('detail', views.detail, ),
    path('safe', views.safe, ),
    path('dailylog', views.dailylog, ),
]
