# To run python manage.py runserver
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("camila", views.camila, name="camila"),
    path("new_year", views.new_year, name="new_year"),
    path("greet_v/<str:name>", views.greet_v, name="greet_V"),
    path("<str:name>", views.greet, name="greet")
]
