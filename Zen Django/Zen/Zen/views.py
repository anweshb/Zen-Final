from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# from app1.models import Doctor
from app1.forms import (FeedbackForm,Question1Form,Question2Form,Question3Form,Question4Form,
                        Question5Form,Question6Form,Question7Form,Question8Form,Question9Form)
from time import time as my_timer
from app1.models import (Responses1,Responses2,Responses3,Responses4,
                        Responses4,Responses5,Responses6,Responses8,Responses7,
                        Responses9,Doctor)
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login
def HomePage(request):
    return render(request,'homepage.html')

def RegisterUser(request):
    if request.method =="POST":
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        email_id = request.POST["mail"]
        password1 = request.POST["pass1"]
        password2 = request.POST["pass2"]
        username = request.POST["username"]

        if password1==password2:
            if User.objects.filter(email=email_id).exists():
                messages.info(request,"This Email ID is already Registered!")
                return render("registeruser.html")
            else:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"Username taken!")
                    return render(request,"registeruser.html")
                else:
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,
                                                    email=email_id,password=password1,username=username)
                    user.save()
                    messages.info(request,"User Created!")
                    return render(request,'login.html')
        else:
            messages.info(request,"Passwords Not Matching!")
            return render("registeruser.html")
        return redirect("/")

    else:
        return render(request,'registeruser.html')

def RegisterDoctor(request):
    if request.method == "POST":
        form = DoctorRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/admin')

    else:
        form = DoctorRegistrationForm()
        args = {'form':form}
        return render(request,'registerdoctor.html')


def loginuser(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('getstarted.html')

    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})


def logoutuser(request):
    auth.logout(request)
    return redirect("/")

def about(request):
    return render(request,'about.html')

def feedback(request):
    if request.method =="POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()

    form = FeedbackForm()
    return render(request,'feedback.html',{'form':form})

def getstarted(request):
    return render(request,'getstarted.html')

def qone(request):
    if request.method == "GET":
        global starttime1
        starttime1 = my_timer()
        form = Question1Form()
    elif request.method == "POST":
        form = Question1Form(request.POST)
        global endtime1
        endtime1 = my_timer()
        timespentstr1 = '{0} seconds'.format(endtime1-starttime1)
        form.save(commit=False)
        # form.cleaned_data['timespent1'] = 0
        if form.is_valid():
            q1_response = (form.cleaned_data['question1'])
            a = Responses1(question1=q1_response,timespent1=timespentstr1,username=request.user.get_username())
            a.save()
            # form.fields['timespent1'].initial = timespentstr
            # print("hi")
            # print(timespentstr)
            # form = form.save(commit=True)
            return redirect('question1/question2/')
    else:
        form = Question1Form()

    return render(request,'question1.html',{'form':form})

def qtwo(request):
    if request.method == "GET":
        global starttime2
        starttime2 = my_timer()
        form = Question2Form()
    elif request.method == "POST":
        form = Question2Form(request.POST)
        global endtime2
        endtime2 = my_timer()
        timespentstr2 = '{0} seconds'.format(endtime2-starttime2)
        form.save(commit=False)
        # form.cleaned_data['timespent1'] = 0
        if form.is_valid():
            q2_response = (form.cleaned_data['question2'])
            a = Responses2(question2=q2_response,timespent2=timespentstr2,username=request.user.get_username())
            a.save()
            # form.fields['timespent2'].initial = timespentstr
            # print("hi")
            # print(timespentstr)
            # form = form.save(commit=True)
            return redirect('question1/question2/question3/')

    else:
        form = Question2Form()

    return render(request,'question2.html',{'form':form})

def qthree(request):
    if request.method == "GET":
        global starttime3
        starttime3 = my_timer()
        form = Question3Form()
    elif request.method == "POST":
        form = Question3Form(request.POST)
        global endtime3
        endtime3 = my_timer()
        timespentstr3 = '{0} seconds'.format(endtime3-starttime3)
        form.save(commit=False)
        # form.cleaned_data['timespent1'] = 0
        if form.is_valid():
            q3_response = (form.cleaned_data['question3'])
            a = Responses3(question3=q3_response,timespent3=timespentstr3,username=request.user.get_username())
            a.save()
            # form.fields['timespent3'].initial = timespentstr
            # print("hi")
            # print(timespentstr)
            # form = form.save(commit=True)
            return redirect('question1/question2/question3/question4/')

    else:
        form = Question3Form()

    return render(request,'question3.html',{'form':form})

def qfour(request):
    if request.method == "GET":
        global starttime4
        starttime4 = my_timer()
        form = Question4Form()
    elif request.method == "POST":
        form = Question4Form(request.POST)
        global endtime4
        endtime4 = my_timer()
        timespentstr4 = '{0} seconds'.format(endtime4-starttime4)
        form.save(commit=False)
        # form.cleaned_data['timespent1'] = 0
        if form.is_valid():
            q4_response = (form.cleaned_data['question4'])
            a = Responses4(question4=q4_response,timespent4=timespentstr4,username=request.user.get_username())
            a.save()
            # form.fields['timespent4'].initial = timespentstr
            # print("hi")
            # print(timespentstr)
            # form = form.save(commit=True)
            return redirect('question1/question2/question3/question4/question5/')

    else:
        form = Question4Form()

    return render(request,'question4.html',{'form':form})

def qfive(request):
    if request.method == "GET":
        global starttime5
        starttime5 = my_timer()
        form = Question5Form()
    elif request.method == "POST":
        form = Question5Form(request.POST)
        global endtime5
        endtime5 = my_timer()
        timespentstr5 = '{0} seconds'.format(endtime5-starttime5)
        form.save(commit=False)
        # form.cleaned_data['timespent1'] = 0
        if form.is_valid():
            q5_response = (form.cleaned_data['question5'])
            a = Responses5(question5=q5_response,timespent5=timespentstr5,username=request.user.get_username())
            a.save()
            # form.fields['timespent5'].initial = timespentstr
            # print("hi")
            # print(timespentstr)
            # form = form.save(commit=True)
            return redirect('question1/question2/question3/question4/question5/question6/')
    else:
        form = Question5Form()

    return render(request,'question5.html',{'form':form})

def qsix(request):
    if request.method == "GET":
        global starttime6
        starttime6 = my_timer()
        form = Question6Form()
    elif request.method == "POST":
        form = Question6Form(request.POST)
        global endtime6
        endtime6 = my_timer()
        timespentstr6 = '{0} seconds'.format(endtime6-starttime6)
        form.save(commit=False)
        if form.is_valid():
            q6_response =form.cleaned_data['question6']
            a = Responses6(question6=q6_response,timespent6=timespentstr6,username=request.user.get_username())
            a.save()
            return redirect('question1/question2/question3/question4/question5/question6/question7/')

    else:
        form = Question6Form()

    return render(request,'question6.html',{'form':form})

def qseven(request):
    if request.method == "GET":
        global starttime7
        starttime7 = my_timer()
        form = Question7Form()
    elif request.method == "POST":
        form = Question7Form(request.POST)
        global endtime7
        endtime7 = my_timer()
        timespentstr7 = '{0} seconds'.format(endtime7-starttime7)
        form.save(commit=False)
        # form.cleaned_data['timespent1'] = 0
        if form.is_valid():
            q7_response = (form.cleaned_data['question7'])
            a = Responses7(question7=q7_response,timespent7=timespentstr7,username=request.user.get_username())
            a.save()
            return redirect('question1/question2/question3/question4/question5/question6/question7/question8')

    else:
        form = Question7Form()

    return render(request,'question7.html',{'form':form})

def qeight(request):
    if request.method == "GET":
        global starttime8
        starttime8 = my_timer()
        form = Question8Form()
    elif request.method == "POST":
        form = Question8Form(request.POST)
        global endtime8
        endtime8 = my_timer()
        timespentstr8 = '{0} seconds'.format(endtime8-starttime8)
        form.save(commit=False)
        if form.is_valid():
            q8_response = (form.cleaned_data['question8'])
            a = Responses8(question8=q8_response,timespent8=timespentstr8,username=request.user.get_username())
            a.save()
            return redirect('question1/question2/question3/question4/question5/question6/question7/question9')

    else:
        form = Question8Form()

    return render(request,'question8.html',{'form':form})

def qnine(request):
    if request.method == "GET":
        global starttime9
        starttime9 = my_timer()
        form = Question9Form()
    elif request.method == "POST":
        form = Question9Form(request.POST)
        global endtime9
        endtime9 = my_timer()
        timespentstr9 = '{0} seconds'.format(endtime9-starttime9)
        form.save(commit=False)
        if form.is_valid():
            q9_response = (form.cleaned_data['question9'])
            a = Responses9(question9=q9_response,timespent9=timespentstr9,username=request.user.get_username())
            a.save()

            return render(request,"recorded.html")

    else:
        form = Question9Form()

    return render(request,'question9.html',{'form':form})
