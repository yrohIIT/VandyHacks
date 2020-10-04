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
            f_name = 'John', 
            l_name = 'Doe', 
            zipcode = 11378, 
            contact_info = 1, 
            online = 1,  
            major = 'CS', 
            school_year = 2020, 
            description = 'test example', 
        )
        newstudent.save()

def mentor_register():
    if request.method == 'POST': 
        newmentor = mentor.objects.create (
            user = request.user, 
            f_name = 'first_name', 
            l_name = 'last_name', 
            education = 'education', 
            zipcode = 'zipcode', 
            Credentials = 'Credentials', 
            contact_info = 'contact_info', 
            area_of_interest = 'area_of_interest'

        )
        newmentor.save()
        return


def student_register():
    if request.method == 'POST': 
        newstudent = student.objects.create (
            user = request.user, 
            f_name = 'first_name', 
            l_name = 'last_name', 
            major = 'major', 
            zipcode = 'zipcode', 
            school_year = 'school_year', 
            contact_info = 'contact_info', 
            area_of_interest = 'area_of_interest'

        )
        newstudent.save()
        return
        



