from django import forms 
from django.contrib.auth.models import User
from .models import student, mentor

class student(Forms.ModelForm):
    Fname = Forms.ModelForm.CharField(max_length = 10)
    Lname = models.CharField(max_length = 10)
    major = models.CharField(max_length = 20)
    online =  models.IntegerField()
    zipcode =  models.IntegerField()
    schoolYear = models.IntegerField()
    contactInfo = models.IntegerField()
    description = models.CharField(max_length = 100)
    user = models.OneToOneField(User,on_delete= models.CASCADE)
