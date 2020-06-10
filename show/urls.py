from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path("456/",views.world),
    path("", views.hello)
]