from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path('html/', html_page),
    path('add/', add_record, name="add"),
]