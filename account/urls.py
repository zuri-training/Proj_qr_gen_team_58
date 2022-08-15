from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
 path('login/', auth_views.LoginView.as_view(), name='login'),
 path('logout/', auth_views.LogoutView.as_view(template_name="registration\logout.html"), name='logout'),
#  path('logout/', views.logout_user, name='logout'),
 path('', views.dashboard, name='dashboard'),
 #  changing password urls
 path('password_reset/', auth_views.PasswordResetView.as_view(template_name="registration\password_reset.html"), name='password_reset'),
 path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="registration\password_reset_don.html"), name='password_reset_done'),
 path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration\password_reset_confim.html"), name='password_reset_confirm'),
 path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="registration\password_reset_complet.html"), name='password_reset_complete'),
 path('register/', views.register, name='register'),
]