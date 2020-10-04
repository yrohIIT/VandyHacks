from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from .models import Student, Mentor, User, Match 

def register(request):
    if request.method == 'POST':

        newuser = User.objects.create_user (
            request.POST.get('username'),
            "email@email.com",
            request.POST.get('password'),
        )
        newuser.save()
        login(request,newuser)
        if request.POST.get('student'):
            return render(request, 'register/student_register.html')
        else:
            return render(request, 'register/mentor_register.html')

    return render(request, 'register/register.html')

def mentor_register(request):
    if request.method == 'POST': 
        newmentor = Mentor.objects.create (
            user = request.user, 
            Fname = request.POST.get('first_name'), 
            Lname = request.POST.get('last_name'), 
            education = request.POST.get('education'), 
            zipcode = request.POST.get('zipcode'), 
            Credentials = request.POST.get('Credentials'), 
            contactInfo = request.POST.get('contact_info'),
            online = int(request.POST.get('online'))

        )
        newmentor.save()
        return HttpResponseRedirect(reverse("dashboard/dashboard", args=(request.user.mentor.user_id,)))


def student_register(request):
    if request.method == 'POST': 
        newstudent = Student.objects.create (
            user = request.user, 
            Fname = request.POST.get('first_name'), 
            Lname = request.POST.get('last_name'), 
            major = request.POST.get('major'), 
            zipcode = request.POST.get('zipcode'), 
            schoolYear = request.POST.get('school_year'), 
            contactInfo = request.POST.get('contact_info'),
            online = int(request.POST.get('online'))

        )
        newstudent.save()
        print("here")
        return HttpResponseRedirect(reverse("match_page"))
        



