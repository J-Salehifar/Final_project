
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ProfileForm, RegisterForm, LoginForm, UserForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_user(request):
    template_name='accounts/login.html'
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            if not User.objects.filter(username=username).exists():
                messages.error(request, 'نام کاربری وجود ندارد')
                return render(request, template_name, context)
            else:
                password = form.cleaned_data['password']
                user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else :
                messages.error(request, 'رمز عبور اشتباه است')
        else:
            form = LoginForm()
    return render(request, template_name, context)


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('accounts:me')
    template_name='accounts/register.html'
    context = {}
    form = RegisterForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            age = form.cleaned_data['age']
            national_code = form.cleaned_data['national_code']
            mobile_number = form.cleaned_data['mobile_number']
            bio = form.cleaned_data['bio']
            gender = form.cleaned_data['gender']
            resume = form.cleaned_data['resume']
            
            if age:
                 user.profile.age = age
            else :
                 messages.ERROR(request,'سن وارد نشده است')
            
            if national_code :
                user.profile.national_code = national_code
            else :
                 messages.ERROR(request,'کد ملی وارد نشده است')

            if mobile_number:
                user.profile.mobile_number = mobile_number
            else :
                 messages.ERROR(request,'شماره موبایل وارد نشده است')                
            
            if bio:
                user.profile.bio = bio
            else:
                user.profile.bio = ''

            if gender :
                 user.profile.gender = gender
            else :
                 messages.ERROR(request,'جنسیت مشخص نشده است')                 

            if resume:
                user.profile.resume = resumeگ  
            
            user.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user) 
            return redirect('accounts:me')
        else:
            form = RegisterForm()
    context['form'] = form
    return render(request,template_name,context)


@login_required()
def profile_view(request):
    template_name='accounts/profile.html'
    context = {}
    user_form = UserForm(request.POST or None, instance=request.user)
    profile_form = ProfileForm(request.POST or None, instance=request.user.profile)
    if request.method == 'POST':
        if user_form.is_valid():
            user_form.save()
        if profile_form.is_valid():
            profile_form.save()
            return redirect('accounts:me')
    context['user_form'] = user_form
    context['profile_form'] = profile_form

    return render(request,template_name,context)

    