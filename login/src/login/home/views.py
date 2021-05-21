from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.
def index(request):
    return render(request,'index.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect("/profile")
        else:
            return render(request,'login.html')        


    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    print("logout")
    return redirect("/login")
    print("logout12")

def profile(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")

    return render(request,'profile.html')