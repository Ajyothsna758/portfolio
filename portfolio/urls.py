from django.urls import path
from . import views

urlpatterns=[
    path("", views.home, name="home"),
    path("certificates/", views.certificates_view, name="certificates"),
    path("contact-me/", views.contact_me, name="contact"),
]