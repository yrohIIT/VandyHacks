from typing import Match
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def dashboard(request, username):
    user = request.user
    if Student.objects.filter(username=username).exists():
        student = Student.objects.get(username=username)
        timeSlots = student.timeSlot
        interests = student.interests

        owner = user.username == student.username
        
        mentors = student.mentor.all()

        return render(request,"dashboard/studentProfile.html", {
            "student":student,
            "timeSlots":timeSlots,
            "interests":interests,
            "mentors":mentors,
            "owner":owner
        })
    if Mentor.objects.filter(username=username).exists():
        mentor = Mentor.objects.get(username=username)
        timeSlots = student.timeSlot
        interests = student.interests

        owner = user.username == student.username
        mentees = mentor.mentee.all()

        return render(request,"dashboard/mentorProfile.html", {
            "mentor":mentor,
            "timeSlots":timeSlots,
            "interests":interests,
            "mentees":mentees,
            "owner":owner
        })

    return render(request, "dashboard/errorProfile.html", {
        "message":"user does not exit."
    })

def edit(request):
    return render(request, "dashboard/edit.html")

def removeMentor(request,mentorId):
    user = request.user
    if Mentor.objects.get(pk=mentorId) is None:
        return render(request, "dashboard/error.html", {
            "message":"Mentor does not exit."
        }) 
    mentor = Mentor.objects.get(pk=mentorId)
    Student.objects.filter(user=user, mentor=mentor).delete()
    return HttpResponseRedirect(reverse("dashboard"))

def removeMentee(request,menteeId):
    user = request.user
    if Student.objects.get(pk=menteeId) is None:
        return render(request, "dashboard/error.html", {
            "message":"Mentee does not exit."
        }) 
    Student.objects.filter(mentor=user, pk=menteeId).delete()
    return HttpResponseRedirect(reverse("dashboard"))