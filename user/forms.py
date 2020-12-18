from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user.models import Profile,employerProfile,addJob



class registrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]


class loginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

    def clean(self):
        print("inside clean")

class createProfileForm(ModelForm):
    user= forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    class Meta:
        model=Profile
        fields="__all__"


class employerRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]


class addJobForm(ModelForm):
    # user= forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = addJob
        fields =["user","company_name","job_title","skills","experience","job_details","phonenumber","email_id",]

class searchForm(ModelForm):
    class Meta:
        model=addJob
        fields=["company_name","job_title","skills","experience"]