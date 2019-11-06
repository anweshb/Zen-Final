"""Zen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.HomePage,name="home"),
    path("registeruser.html/",views.RegisterUser,name='registeruser'),
    path("registerdoctor.html/",views.RegisterDoctor,name='registerdoctor'),
    path("login/",views.loginuser,name='login'),
    path("logoutuser/",views.logoutuser,name='logout'),
    path('aboutus/',views.about,name='about'),
    path('feedback/',views.feedback,name='feedback'),
    path('login/getstarted.html/',views.getstarted,name='getstarted'),
    path('question1/', views.qone, name='qone'),
    path('question1/question1/question2/',views.qtwo, name='qtwo'),
    path('question1/question1/question2/question1/question2/question3/',views.qthree,name='qthree'),
    path('question1/question1/question2/question1/question2/question3/question1/question2/question3/question4/',views.qfour,name='qfour'),
    path('question1/question1/question2/question1/question2/question3/question1/question2/question3/question4/question1/question2/question3/question4/question5/',views.qfive,name='qfive'),
    path('question1/question1/question2/question1/question2/question3/question1/question2/question3/question4/question1/question2/question3/question4/question5/question1/question2/question3/question4/question5/question6/',views.qsix,name='qsix'),
    path('question1/question1/question2/question1/question2/question3/question1/question2/question3/question4/question1/question2/question3/question4/question5/question1/question2/question3/question4/question5/question6/question1/question2/question3/question4/question5/question6/question7/',views.qseven,name='qseven'),
    path('question1/question1/question2/question1/question2/question3/question1/question2/question3/question4/question1/question2/question3/question4/question5/question1/question2/question3/question4/question5/question6/question1/question2/question3/question4/question5/question6/question7/question1/question2/question3/question4/question5/question6/question7/question8',views.qeight,name='qeight'),
    path('question1/question1/question2/question1/question2/question3/question1/question2/question3/question4/question1/question2/question3/question4/question5/question1/question2/question3/question4/question5/question6/question1/question2/question3/question4/question5/question6/question7/question1/question2/question3/question4/question5/question6/question7/question1/question2/question3/question4/question5/question6/question7/question9',views.qnine,name='qnine')
]
