from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]


            user = Account.objects.create_user(first_name=first_name,last_name=last_name,
                                               username=username,email=email,
                                               password=password)
            user.phone_number = phone_number
            user.save()
            messages.success(request,'Registration Successful')
            return redirect('login')

    else:

        form = RegistrationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/register.html',context)

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            # messages.success(request,'Login Successful')
            return redirect('home')
        else:
            messages.error(request,'invalid login credential')
            return redirect('login')

    return render(request,'accounts/login.html')


def user_logout(request):
    logout(request)
    messages.success(request,'You are logged out')
    return redirect('login')



