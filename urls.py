from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard-home'),
    path('bicing/', views.bicing, name='bicing-home'),
]