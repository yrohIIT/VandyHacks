from django.shortcuts import render
from .models import student, mentor 

def register(request):
    if request.method == 'POST':
        
        if request.POST.get('student'):
            return render(request, 'register/student_register.html')
        else:
            return render(request, 'register/mentor_register.html')
        #return
    return render(request, 'register/register.html')
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

def mentor_register():
    if request.POST.get('first_name', 'last_name','education', 'zipcode' 'Credentials', 'contact_info', 'area_of_interest'):
        return 

def student_register():
    if request.POST.get('first_name', 'last_name', 'major', 'zipcode', 'school_year', 'contact_info', 'area_of_interest'):
        return



