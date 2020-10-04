from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    Fname = models.CharField(max_length = 10)
    Lname = models.CharField(max_length = 10)
    major = models.CharField(max_length = 20)
    online =  models.IntegerField()
    zipcode =  models.IntegerField()
    schoolYear = models.IntegerField()
    contactInfo = models.IntegerField()
    description = models.CharField(max_length = 100)
    user = models.OneToOneField(User,on_delete= models.CASCADE)

# def create_user_student(sender,instance, created, **kwargs):
#     if kwargs.get('created', False):
#         student.objects.create(user=instance)

class Mentor(models.Model):
    Fname = models.CharField(max_length = 10)
    Lname = models.CharField(max_length = 10)
    education = models.CharField(max_length = 40)
    online =  models.IntegerField()
    zipcode =  models.IntegerField()
    credentials = models.IntegerField()
    contactInfo = models.IntegerField()
    description = models.CharField(max_length = 100)
    user = models.OneToOneField(User,on_delete= models.CASCADE)



# Create your models here.
class Match(models.Model):
    student = models.IntegerField()
    mentor = models.IntegerField()
    student_yes = models.IntegerField()
    mentor_yes = models.IntegerField()