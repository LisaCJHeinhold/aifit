from django.shortcuts import render, redirect
from fire.firebase import firebaseInit
from django.contrib import auth
from fire.firebase_auth import verify_id_token
from django.conf import settings


def login(request):
    firebase_config = settings.FIREBASE_CONFIG
    if request.method == 'POST':
        id_token = request.POST.get('id_token')
        user = verify_id_token(id_token)
        if user:
            auth.login(request, user)
            return redirect('dashboard')  # Redirect to dashboard page after login
        else:
            # Handle invalid login
            pass
    return render(request, 'aifit_app/login.html')

def signup(request):
    # Implement signup logic here
    pass

def logout(request):
    auth.logout(request)
    return redirect('login')

def home(request):
    firebaseInit()
    return render(request, 'aifit_app/index.html')