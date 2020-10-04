from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Student, Mentor, User, Match 

def register(request):
    if request.method == 'POST':
        return 
    if request.user.is_authenticated:
        newstudent = Student.objects.create(
            user = request.user, 
            Fname = 'John', 
            Lname = 'Doe', 
            zipcode = 11378, 
            contactInfo = 1, 
            online = 1,  
            major = 'CS', 
            schoolYear = 2020, 
            description = 'test example', 
        )
        newstudent.save()
