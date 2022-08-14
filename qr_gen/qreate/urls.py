from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('user_cases/', views.user_cases, name='user_cases'),
    path('features/', views.features, name='features'),
    path('show_qr/',views.show_qr, name='show_qr'),
    path('add_qr/', views.add_qr, name='add_qr'),
    path('created/', views.created_qr, name='created_qr'),
    path('qr_pdf/<pk>/', views.qr_pdf, name='qr_pdf'),
    path('qr_jpg/<pk>/', views.qr_jpg, name='qr_jpg'),
    path('Terms_of_Service/', views.Terms_of_Service, name='Terms_of_Service'),
    path('Privacy_Policy/', views.Privacy_Policy, name='Privacy_Policy'),
]
