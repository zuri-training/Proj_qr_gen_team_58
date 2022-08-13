from . import views
from django.urls import path

urlpatterns = [
    path('', views.support, name="support"),
]
