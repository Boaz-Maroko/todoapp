from django.shortcuts import render, redirect, HttpResponse
from .forms import SignUpForm, SignInForm

from django.contrib.auth import login, logout, authenticate

# Create your views here.

def signup(request):
    """
    Collects the user creation data and sends it to the User model where it 
    is saved as a user instance object
    """
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid:
            form.save()
            return redirect("accounts:signin")

        else:
            form.add_error(field='username', error="User exists")
            return render(request, 'accounts/signup.html', {"form": form})
    else:
        form = SignUpForm()
        return render(request, "accounts/signup.html", {"form": form})
    

# A view to collect user info and if valid log them in

def signin(request):
    """
    collect user info and login in user if
    info is valid
    """
    if request.method == "POST":
        form = SignInForm(request.POST)

        if form.is_valid():
            # for field, error in form.errors:
            try:

                user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return HttpResponse("Login was successful")
                else:
                    raise ValueError("The credentials are in valid")
            except Exception as e:
    
                form.add_error(field='username', error=e)
                return render(request, 'accounts/signin.html', {"form": form})
        else:
            return render(request, 'accounts/signin.html', {"form": form})
    else:
        form = SignInForm()
        return render(request, 'accounts/signin.html', {"form": form})
    



    
