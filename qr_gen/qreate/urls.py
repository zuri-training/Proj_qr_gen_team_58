from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    # path('', views.home, name='home'),
    path('show_email_qr/', views.email_qr, name='show_email_qr'),
    path('show_qr/',views.generate_web_qr, name='show_qr'),
=======
    path('', views.home, name='home'),
    # path('show_email_qr/', views.email_qr, name='show_email_qr'),
    path('show_qr/',views.show_qr, name='show_qr'),
>>>>>>> 510e10562d11087730b7722332029d5d483733bd
    path('add_qr/', views.add_qr, name='add_qr'),
    path('created/', views.created_qr, name='created_qr'),
    path('qr_pdf/<pk>/', views.qr_pdf, name='qr_pdf'),
    path('qr_jpg/<pk>/', views.qr_jpg, name='qr_jpg'),
]
