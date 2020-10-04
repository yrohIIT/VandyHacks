from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Student, Mentor, User, Match 

def register(request):
    if request.method == 'POST':
        
        if request.POST.get('student'):
            return render(request, 'register/student_register.html')
        else:
            return render(request, 'register/mentor_register.html')
        #return
    return render(request, 'register/register.html')
    if request.user.is_authenticated:
        newstudent = Student.objects.create(
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

def mentor_register(request):
    if request.method == 'POST': 
        newmentor = Mentor.objects.create (
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
        return HttpResponseRedirect(reverse("dashboard/dashboard", args=(request.user.mentor.user_id,)))


def student_register(request):
    if request.method == 'POST': 
        newstudent = Student.objects.create (
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
        print("here")
        return HttpResponseRedirect(reverse("match_page"))
        



