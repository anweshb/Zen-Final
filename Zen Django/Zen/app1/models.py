from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.conf import settings
#first_name,last_name,email_id,phone_no,exp,password,confirmc

# Create your models here.

class Doctor(AbstractBaseUser):
    first_name = models.CharField(default="",max_length=30,required=True)
    last_name = models.CharField(default="",max_length=30,required=True)
    email_id = models.EmailField(max_length=40,unique=True)
    username = models.CharField(max_length=30,unique=True)
    phone_no = models.IntegerField(unique=True)
    exp = models.IntegerField(choices=[('0','0'),('2+','2+'),('5+','5+'),('10+','10+')])
    date_joined = models.DateTimeField(verbose_name = 'date joined',auto_now_add = True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Feedback(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    type = models.CharField(choices=[('Technical','Technical'),('Non-Technical','Non-Technical'),('Other','Other')],max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

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
