from django.urls import path
from . import views

urlpatterns = [
    # This matches the 'cities/' path and calls the index function in views.py
    path('', views.index, name='cities_index'),
    path('<int:city_id>/', views.detail, name='city_detail')
]