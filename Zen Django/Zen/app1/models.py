from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.conf import settings
#first_name,last_name,email_id,phone_no,exp,password,confirmc

# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete='models.CASACDE')
    phone_no = models.IntegerField(unique=True)
    user_type = models.TextField(default='Doctor')

class Feedback(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    type = models.CharField(choices=[('Technical','Technical'),('Non-Technical','Non-Technical'),('Other','Other')],max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.user.username

class Responses1(models.Model):
    username = models.TextField(default="")
    question1 = models.TextField(default="")
    timespent1 = models.TextField(default=0)

class Responses2(models.Model):
    username = models.TextField(default="")
    question2 = models.TextField(default="")
    timespent2 = models.TextField(default=0)

class Responses3(models.Model):
    username = models.TextField(default="")
    question3 = models.TextField(default="")
    timespent3 = models.TextField(default=0)

class Responses4(models.Model):
    username = models.TextField(default="")
    question4 = models.TextField(default="")
    timespent4 = models.TextField(default=0)

class Responses5(models.Model):
    username = models.TextField(default="")
    question5 = models.TextField(default="")
    timespent5 = models.TextField(default=0)

class Responses6(models.Model):
    username = models.TextField(default="")
    question6 = models.TextField(default="")
    timespent6 = models.TextField(default=0)

class Responses7(models.Model):
    username = models.TextField(default="")
    question7 = models.TextField(default="")
    timespent7 = models.TextField(default=0)

class Responses8(models.Model):
    username = models.TextField(default="")
    question8 = models.TextField(default="")
    timespent8 = models.TextField(default=0)

class Responses9(models.Model):
    username = models.TextField(default="")
    question9 = models.TextField(default="")
    timespent9 = models.TextField(default=0)
