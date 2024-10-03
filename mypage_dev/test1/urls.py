from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.file_give),
    path('file_show/', views.file_show)
]
