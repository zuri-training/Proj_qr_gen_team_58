from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('show_email_qr/', views.email_qr, name='show_email_qr'),
    path('show_qr/',views.generate_web_qr, name='show_qr'),
    path('add_qr/', views.add_qr, name='add_qr'),
    path('created/', views.created_qr, name='created_qr'),

]
