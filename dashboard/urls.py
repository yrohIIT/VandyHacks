from django.urls import path

from . import views

urlpatterns = [
    path("<str:username>", views.dashboard, name="dashboard"),
    path("edit", views.dashboard, name="edit"),
    path("removeMentor/<int:mentorId>", views.removeMentor, name="removeMentor"),
    path("removeMentee/<int:menteeId>", views.removeMentee, name="removeMentee")
]