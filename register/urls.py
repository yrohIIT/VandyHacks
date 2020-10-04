# include imports, url 
from django.conf.urls import url 
from . import views
urlpatterns = [
    url(r'^register', views.register, name='register'),
    url(r'^student_register', views.student_register, name ='student'),
    url(r'^mentor_register', views.mentor_register, name ='mentor')
] 