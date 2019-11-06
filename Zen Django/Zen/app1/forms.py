from django import forms
from app1.models import Feedback,Doctor
from app1.models import (Responses1,Responses2,Responses3,Responses4,
                        Responses4,Responses5,Responses6,Responses8,Responses7,
                        Responses9)


class FeedbackForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Feedback
        fields = ('name','email','type','description')

class DoctorRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Doctor
        fields = ('first_name','last_name','phone_no','email_id','username',
                    'phone_no','exp')


class Question1Form(forms.ModelForm):
    question1 = forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control'}))
    timespent1 = forms.CharField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Responses1
        fields = ('question1','timespent1',)

class Question2Form(forms.ModelForm):
    question2 = forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control'}))
    timespent2 = forms.CharField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Responses2
        fields = ('question2','timespent2')

class Question3Form(forms.ModelForm):
    question3 = forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control'}))
    timespent3 = forms.CharField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Responses3
        fields = ('question3','timespent3')

class Question4Form(forms.ModelForm):
    question4 = forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control'}))
    timespent4 = forms.CharField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Responses4
        fields = ('question4','timespent4')

class Question5Form(forms.ModelForm):
    question5 = forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control'}))
    timespent5 = forms.CharField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Responses5
        fields = ('question5','timespent5')

class Question6Form(forms.ModelForm):
    question6 = forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control'}))
    timespent6 = forms.CharField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Responses6
        fields = ('question6','timespent6')

class Question7Form(forms.ModelForm):
    question7 = forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control'}))
    timespent7 = forms.CharField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Responses7
        fields = ('question7','timespent7')

class Question8Form(forms.ModelForm):
    question8 = forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control'}))
    timespent8 = forms.CharField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Responses8
        fields = ('question8','timespent8')

class Question9Form(forms.ModelForm):
    question9 = forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control'}))
    timespent9 = forms.CharField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Responses9
        fields = ('question9','timespent9')
