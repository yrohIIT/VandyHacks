from django.urls import path
from django.conf.urls import url 

from . import views

urlpatterns = [
    path("<int:userId>", views.dashboard, name="dashboard"),
    path("edit", views.dashboard, name="edit"),
    path("login", views.login_view, name="login"),
    path("match_page", views.match_page, name="match_page"),
    path("logout", views.logout_view, name="logout")
]