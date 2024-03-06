from django.shortcuts import render, redirect
from fire.firebase import firebaseInit, Firebase
from django.contrib import messages
import firebase_admin
from firebase_admin import auth

def home(request):
    # firebaseInit()
    # Assuming the credentials file is located at 'path/to/your/credentials.json'
    firebase_instance = Firebase()
    print(firebase_instance)
    
     # Now you can use the firebase_instance to interact with Firebase services
    data = firebase_instance.get_data(collection='your_collection', document='your_document')
    print(data)
    
    return render(request, 'aifit_app/index.html')

def login(request):
    # firebaseInit()
    print("login was called")

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = auth.get_user_by_email(email)
            print("user exists", user)
            messages.success(request, "Login successful!")
            # auth.verify_password(user.uid, password)
            # print("user password authenticated")
            return redirect('dashboard')
        except Exception as e:
            print("user does not exist")
            messages.error(request, "Invalid email or password. Please try again.")
            return render(request,'aifit_app/login.html')

    return render(request,'aifit_app/login.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = auth.create_user(email=email, password=password)
            messages.success(request, "Sign-up successful!")
            return redirect('login')
        except Exception as e:
            messages.error(request, "Sign-up failed. Please try again.")
            return render(request,'aifit_app/signup.html')
        
    return render(request,'aifit_app/signup.html')

def logout(request):
    return render(request,'aifit_app/login.html')

def dashboard(request):
    return render(request,'aifit_app/dashboard.html')

def chat(request):
    return render(request,'aifit_app/chat.html')

def profile(request):
    return render(request,'aifit_app/profile.html')

def goals(request):
    return render(request,'aifit_app/goals.html')

def graph(request):
    return render(request,'aifit_app/graph.html')

def previous_workouts(request):
    return render(request,'aifit_app/previousworkouts.html')