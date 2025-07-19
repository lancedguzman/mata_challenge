from django.urls import path
from .views import base_template

urlpatterns = [
    path("", base_template, name="base"),
]