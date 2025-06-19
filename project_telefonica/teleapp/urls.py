from django.urls import path
from . import views

urlpatterns = [
    path('load-csv/', views.load_mobile_towers_from_csv, name='load_csv'),
    path('', views.tower_map, name='tower_map'),
]
