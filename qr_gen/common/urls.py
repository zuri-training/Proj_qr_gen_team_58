from . import views
from django.urls import path, include

urlpatterns = [
    path("contact/", views.contact, name="contact_page"),
]
