from django.contrib.auth.signals import user_logged_in
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from register.models import Student, Mentor, Match, User

# Create your views here.
def dashboard(request, userId):
    user = request.user
    if Student.objects.filter(user_id=userId).exists():
        student = Student.objects.get(user_id=userId)
        match_list = Match.objects.filter(student=user.id)
        mentors = []
        for i in range(len(match_list)):
            mentors.append(Mentor.objects.get(user_id=match_list[i].mentor))

        return render(request,"dashboard/studentProfile.html", {
            "student":student,
            "mentors":mentors

        })
    if Mentor.objects.filter(user_id=userId).exists():
        mentor = Mentor.objects.get(user_id=userId)
        match_list = Match.objects.filter(mentor=user.id)
        students = []
        for i in range(len(match_list)):
            students.append(Student.objects.get(user_id=match_list[i].student))
        
        return render(request,"dashboard/mentorProfile.html", {
            "mentor":mentor,
            "students":students
        })

    return render(request, "dashboard/errorProfile.html", {
        "message":"user does not exit."
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("dashboard", args=(user.id,)))
        else:
            return render(request, "dashboard/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "dashboard/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def find_match(s_user):
    mentor_list = Mentor.objects.all()

    # Filtering
    if s_user.student.online != 0:
        mentor_list = mentor_list.filter(zipcode=s_user.student.zipcode)
    
    # Check if already matched
    match_list = []
    for i in range(len(mentor_list)):
        m_user = User.objects.filter(id=mentor_list[i].user_id)
        if not Match.objects.filter(student=s_user.id, mentor=m_user[0].id).exists():
           match_list.append(mentor_list[i])

    return match_list

def match_page(request):
    mentor_list = find_match(request.user)
    context = {}
    if request.method == "POST":

        if request.POST.get('profile'):
            context["student"] = request.user.student
            return HttpResponseRedirect(reverse("dashboard", args=(request.user.student.user_id,)))

        student = request.user
        mentor_id = request.POST.get('mentor')
        mentor = get_object_or_404(Mentor,id=mentor_id)
        if request.POST.get('yes'):
            match = Match.objects.create(student=student.student.user_id, mentor=mentor.user_id, student_yes=1, mentor_yes=0)
            match.save()
            print("here")
        elif request.POST.get('no'):
            match = Match.objects.create(student=student.user_id, mentor=mentor.user_id, student_yes=0, mentor_yes=0)
            match.save()
        context['mentor'] = mentor_list[1]
        
        return render(request, 'register/match_page.html', context)

    else:
        context['mentor'] = mentor_list[0]
        print(mentor_list)
        return render(request, 'register/match_page.html', context)
        