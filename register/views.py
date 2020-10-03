from django.shortcuts import render
from .models import student, mentor 

def register(request):
    if request.method == 'POST':
        return 
    if request.user.is_authenticated:
        newstudent = student.objects.create(
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
        
