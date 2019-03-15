from django.urls import path
from flowerapp import views

urlpatterns = [
    path('', views.home, name='lv-home'),
    path('flower_prediction/', views.prediction, name='flower_prediction'),
]
