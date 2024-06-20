from django.urls import path

from . import views


urlpatterns = [
    path("", views.no, name="no"),
    path("test/", views.index, name="index"),
    path("test2/", views.test, name="test"),
]