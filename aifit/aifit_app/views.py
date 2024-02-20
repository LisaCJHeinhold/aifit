from django.shortcuts import render, redirect
from fire.firebase import firebaseInit, Firebase
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
    # firebaseInit()
    # Assuming the credentials file is located at 'path/to/your/credentials.json'
    firebase_instance = Firebase()
    print(firebase_instance)
    
     # Now you can use the firebase_instance to interact with Firebase services
    data = firebase_instance.get_data(collection='your_collection', document='your_document')
    print(data)
    
    return render(request, 'aifit_app/index.html')