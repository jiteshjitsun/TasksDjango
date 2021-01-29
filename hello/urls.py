from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("jitesh", views.jitesh, name="Jitesh"),
    path("<str:name>", views.greet, name="Greet")
]