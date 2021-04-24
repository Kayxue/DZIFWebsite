from django.urls import *
from .views import *

urlpatterns = [
    path("", Home.as_view(), name="home")
]
