from django.urls import path
from . import views

urlpatterns = [
    path("",views.logIn, name="logIn"),
    path("index/",views.index, name="index"),
    path("newTask/", views.newTask, name="newTask"),
    path("newUser/", views.newUser, name="newUser"),
    path("update/<int:id>/", views.update, name="update"),
    path("delete/<int:id>/", views.delete, name="delete"),
]