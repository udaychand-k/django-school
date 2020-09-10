from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')
def register(request):
    if request.method == 'POST':
        firstname = request.POST["fn"];
        lastname = request.POST['ln'];
        username = request.POST['un'];
        email = request.POST['e'];
        password = request.POST['p'];
        confirm_password= request.POST['cp'];

        if password != confirm_password:
            messages.info(request,"Password didn't matched! please give again");
            return redirect('/register/')
        else:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists');
                return redirect('/register/')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'entered email is already exists');
                return redirect('/register/');
            else:
                user = User.objects.create_user(username = username,password=password,email=email,first_name=firstname,last_name=lastname);
                user.save();
                messages.info(request,'successfully registered')
                return redirect('/home')

    else:
        return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        username=request.POST['un'];
        password = request.POST['p'];
        user=auth.authenticate(username=username,password=password);

        if user is not None:
            auth.login(request,user);
            messages.success(request,'successfully Login')
            return redirect('/home');
        else:
            messages.info(request,'Failed to Login')
            return redirect('/login')

    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request);
    messages.info(request,'You have Logout successfully')
    return redirect('/home')
def about(request):
    return render(request,'about.html')
