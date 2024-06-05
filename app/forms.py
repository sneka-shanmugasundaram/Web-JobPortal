from typing import Any
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import forms



class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =("username","email","password1","password2")



    
    def __init__(self, *args: Any, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder']='Username'
        self.fields['email'].widget.attrs['placeholder']='Email'
        self.fields['password1'].widget.attrs['placeholder']='Password'
        self.fields['password2'].widget.attrs['placeholder']='Confirm Password'
    
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise forms.ValidationError("username already exits")
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise forms.ValidationError("email already exits")
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2 :
            raise forms.ValidationError("password don't match")
        return password2

class close(ModelForm):
    class Meta:
        model=JobPost
        fields=("status",)

class PostForm(ModelForm):
    class Meta:
        model=JobPost
        #fields="__all__"
        fields=("title","c_name","image","description","expiry","salary","slug","location","author","skills","status","type")
    
    
    
    def __init__(self, *args: Any, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder']='Job Title'
        self.fields['title'].label=False
        self.fields['c_name'].widget.attrs['placeholder']='Company Name'
        self.fields['c_name'].label=False
        self.fields['image'].widget.attrs['placeholder']='Company Logo'
        self.fields['image'].label=False
        self.fields['description'].widget.attrs['placeholder']='Description'
        self.fields['description'].label=False
        self.fields['salary'].widget.attrs['placeholder']='salary'
        self.fields['salary'].label=False
        self.fields['slug'].widget.attrs['placeholder']='slug'
        self.fields['slug'].label=False
        self.fields['expiry'].widget.attrs['placeholder']='expriy'
        self.fields['expiry'].label=False


class SaveForm(ModelForm):
    class Meta:
        model=JobTitle
        fields="__all__"
    

    def __init__(self, *args: Any, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company_name'].widget.attrs['placeholder']='Enter User Name'
        self.fields['company_name'].label=False
        self.fields['name'].widget.attrs['placeholder']='Enter jobtitle !!'
        self.fields['name'].label=False

class LocationForm(ModelForm):
    class Meta:
        model=Location
        fields="__all__" 

    def __init__(self, *args: Any, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['street'].widget.attrs['placeholder']='street'
        self.fields['street'].label=False
        self.fields['city'].widget.attrs['placeholder']='city'
        self.fields['city'].label=False
        self.fields['state'].widget.attrs['placeholder']='state'
        self.fields['state'].label=False
        self.fields['country'].widget.attrs['placeholder']='country'
        self.fields['country'].label=False
        self.fields['zip'].widget.attrs['placeholder']='zip'
        self.fields['zip'].label=False


class AuthorForm(ModelForm):
    class Meta:
        model=Author
        fields="__all__"
    

    def __init__(self, *args: Any, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder']='Author Name'
        self.fields['name'].label=False
        self.fields['company'].widget.attrs['placeholder']='Company'
        self.fields['company'].label=False
        self.fields['designation'].widget.attrs['placeholder']='Designation'
        self.fields['designation'].label=False


class SkillForm(ModelForm):
    class Meta:
        model=Skills
        fields="__all__"
    

    def __init__(self, *args: Any, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder']='Skill'
        self.fields['name'].label=False


class ProfileForm (ModelForm):
    class Meta:
        model= Profile
        fields =("image","Full_Name","email","phone_number","objectives","Resume","experience")

    def __init__(self, *args: Any, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Full_Name'].widget.attrs['placeholder']='Full Name'
        self.fields['Full_Name'].label=False
        self.fields['email'].widget.attrs['placeholder']='Email Address'
        self.fields['email'].label=False
        self.fields['phone_number'].widget.attrs['placeholder']='Phone Number'
        self.fields['phone_number'].label=False
        self.fields['objectives'].widget.attrs['placeholder']='Summary Or Objectives'
        self.fields['objectives'].label=False


class CertificationForm(ModelForm):
    class Meta:
        model = Certification
        fields = "__all__"

    def __init__(self, *args: Any, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course_name'].widget.attrs['placeholder']='Name of the Course'
        self.fields['course_name'].label=False
        

class tenth(ModelForm):
    class Meta:
        model = Ten_th
        fields = "__all__"

    def __init__(self, *args: Any, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ten_education'].widget.attrs['placeholder']=' 10th'
        self.fields['ten_education'].label=False
        self.fields['Board'].widget.attrs['placeholder']= 'Board of Education'
        self.fields['Board'].label=False
        self.fields['passing_out_year'].widget.attrs['placeholder']=' Passing_out_year'
        self.fields['passing_out_year'].label=False
        self.fields['school_medium'].widget.attrs['placeholder']=' School Medium'
        self.fields['school_medium'].label=False
        self.fields['total_mark_ten'].widget.attrs['placeholder']=' Total Mark'
        self.fields['total_mark_ten'].label=False