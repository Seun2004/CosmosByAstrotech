from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.
#registration

def register(request):
    if request.user.is_authenticated:
        return redirect("main_cosmos:home")
    # if they arent loggen in already
    else:
        if request.method == "POST":
            form = RegisterForm(request.POST or None)
            #check if form is valid
            if form.is_valid():
                user = form.save()

                #get raw password
                rawpassword = form.cleaned_data.get('password1')

                #authenticate
                user = authenticate(username=user.username, password=rawpassword)

                #log the user in
                login(request, user)

                return redirect("main_cosmos:home")
        else:
            form = RegisterForm()
        return render(request, "useraccounts/register.html", {"form": form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect("main_cosmos:home")
    # if they arent loggen in already
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

     #check credentials
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("main_cosmos:home")

                else:
                    return render(request, 'useraccounts/login.html', {"error": "Account disabled"})
            else:
                return render(request, 'useraccounts/login.html', {"error": "Invalid Username/Password. Try Again"})

        return render(request, 'useraccounts/login.html') 



def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        print("Logout Successful")
        return redirect("useraccounts:login")
    else:
        return redirect("useraccounts:login")
    