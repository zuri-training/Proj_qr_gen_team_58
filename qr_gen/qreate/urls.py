from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('show_qr/', views.show_qr, name='show_qr'),
]
