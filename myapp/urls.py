from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:app_id>/', views.details, name='genre'),
]
