from django import forms
from django.contrib.auth.forms import UserCreationForm, UserModel
from django.forms import ModelForm, fields, models
from django.contrib.auth.models import User
from .models import Profile
from .utils import GENDER_TYPE


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age','national_code','mobile_number','bio','gender','resume']
    # def __init__(self, *args, **kwargs):
    #     super(ProfileForm, self).__init__(*args, **kwargs)
    #     self.fields['national_code'].disabled = True


class RegisterForm(UserCreationForm):
    age = forms.IntegerField(label='سن',max_value=99)
    national_code = forms.CharField(label='کد ملی', max_length=10)
    mobile_number = forms.CharField(label='شماره موبایل', max_length=11)
    bio = forms.CharField(label='معرفی', max_length=150, required=False)
    gender = forms.ChoiceField(label='جنسیت', choices=GENDER_TYPE, required=False)
    resume = forms.FileField(label='رزومه', required=False)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2','age','national_code','mobile_number','bio','gender','resume']



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(),label='نام کاربری')
    password = forms.CharField(widget=forms.PasswordInput(),label='رمز عبور')


