from django.shortcuts import render, redirect
from fire.firebase import firebaseInit, Firebase
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import SignUpForm, UserLoginForm
from firebase_admin import firestore
from django.contrib import auth
from fire.firebase_auth import verify_id_token
from django.conf import settings
from django.http import JsonResponse
import firebase_admin
from firebase_admin import auth, firestore
from django.http import HttpResponse
from django.template import loader
from .models import Workout
from google.cloud.firestore_v1 import SERVER_TIMESTAMP

# def login(request):
#     firebase_config = settings.FIREBASE_CONFIG
#     if request.method == 'POST':
#         id_token = request.POST.get('id_token')
#         user = verify_id_token(id_token)
#         if user:
#             auth.login(request, user)
#             return redirect('dashboard')  # Redirect to dashboard page after login
#         else:
#             # Handle invalid login
#             pass
#     return render(request, 'aifit_app/login.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if email is None or password is None:
            return JsonResponse({"error": "Email or password is missing"}, status=400)

        try:
            user = auth.get_user_by_email(email)
            # Firebase user exists, try to sign in
            user = auth.sign_in_with_email_and_password(email, password)
            # Authentication successful, return user's Firebase UID
            return JsonResponse({"uid": user["localId"]})
        except firebase_admin.auth.UserNotFoundError:
            # Firebase user doesn't exist
            return JsonResponse({"error": "User not found"}, status==400)
    
    return render(request, "aifit_app/login.html")

def signup(request):
    # Implement signup logic here
    pass

def logout(request):
    auth.logout(request)
    return redirect('login')

from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

# GRAPH FUNCTIONS
from django.views import View
#import jsonresponse
from django.http import JsonResponse

class LineChartJSONView(View):
    # This command will get the user's id once the user is logged in
    # -> request.user.id <-
    user_id='hfIg3WidzBTHgezNF8O2'

    def get(self, request, *args, **kwargs):
        db = firestore.client()
        graph_data = db.collection('graph').where('user_id', '==', self.user_id).stream()
        print(graph_data)
        labels = []
        body_fat = []
        muscle_mass = []

        for data in graph_data:
            data_dict = data.to_dict()
            labels.append(data_dict['date_created'])
            body_fat.append(data_dict['body_percentage_fat'])
            muscle_mass.append(data_dict['muscle_mass_percentage'])
            #print(data_dict)

        print(body_fat)
        print(muscle_mass)

        data = {
            "labels": labels,
            "datasets": [
                {
                    "label": "% Body Fat",
                    "data": body_fat,
                    "borderColor": 'blue',
                    "backgroundColor": 'rgba(0, 0, 255, 0.1)'
                },
                {
                    "label": "% Muscle Mass",
                    "data": muscle_mass,
                    "borderColor": 'red',
                    "backgroundColor": 'rgba(255, 0, 0, 0.1)'
                }
            ]
        }

        return JsonResponse(data)

from django.shortcuts import render

def previous_workouts(request):
   
    # This command will get the user's id once the user is logged in
    # -> request.user.id <-
    
    previous_workouts = firestore.client().collection('user_workouts').stream()
    workouts = []
    for workout in previous_workouts:
        workouts_data = workout.to_dict()
        print(workouts_data)
        workouts.append({
            'user_id': workouts_data.get('user_id', ''),
            'type': workouts_data.get('type', ''),
            'time': workouts_data.get('time', ''),
            'date_created': workouts_data.get('date_created', ''),
            'number_exercises': workouts_data.get('number_exercises', ''),
        })
        print(workouts_data.get('type', '')) 
        print(workouts_data.get('number_exercises', ''))
    return render(request, 'aifit_app/previousworkouts.html', {'workouts': workouts})
# # previous workouts function testing
# def workouts(request):
#     previous_workouts = firestore.client().collection('workouts').where('user_id', '== ', 'user_workouts.user_id').stream()
#     workouts = []
#     for workout in previous_workouts:
#         workouts_data = workout.to_dict()
#         workouts.append({
#             'user_id': workouts_data.get('user_id', ''),
#             'type': workouts_data.get('type', ''),
#             'time': workouts_data.get('time', ''),
#             'date_created': workouts_data.get('date_reated', ''),
#             'number_exercises': workouts_data.get('number_exercises', ''),
            
#         })
#         print(workouts_data.get('type', ''))

#     return workouts
#         # workouts=Workout.objects.all()
#         # template = loader.get_template('aifit_app/previousworkouts.html')
#         # context = {'workouts': workouts}
#         # return HttpResponse(template.render(context, request))

line_chart = TemplateView.as_view(template_name='graph.html')
line_chart_json = LineChartJSONView.as_view()
def home(request):
    # firebaseInit()
    # Assuming the credentials file is located at 'path/to/your/credentials.json'
    firebase_instance = Firebase()
    print(firebase_instance)
    
     # Now you can use the firebase_instance to interact with Firebase services
    data = firebase_instance.get_data(collection='your_collection', document='your_document')
    print(data)
    
    return render(request, 'aifit_app/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, user)

            db = firestore.client()
            users_ref = db.dollection(u'users')
            users_ref.document(str(user.id)).set({u'email': form.cleaned_data['email'],})

            return redirect('dashboard')

    else:
        form = SignUpForm()

    return render(request, 'aifit_app/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                pass

    else:
        form = UserLoginForm()

    return render(request, 'aifit_app/login.html', {'form': form})
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     try:
    #         user = auth.create_user(email=email, password=password)
    #         messages.success(request, "Sign-up successful!")
    #         return redirect('login')
    #     except Exception as e:
    #         messages.error(request, "Sign-up failed. Please try again.")
    #         return render(request,'aifit_app/signup.html')
        
    # return render(request,'aifit_app/signup.html')

def logout(request):
    logout(request)
    return redirect('logout')


# def login(request):
#     # firebaseInit()
#     print("login was called")

#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         try:
#             user = auth.get_user_by_email(email)
#             print("user exists", user)
#             messages.success(request, "Login successful!")
#             # auth.verify_password(user.uid, password)
#             # print("user password authenticated")
#             return redirect('dashboard')
#         except Exception as e:
#             print("user does not exist")
#             messages.error(request, "Invalid email or password. Please try again.")
#             return render(request,'aifit_app/login.html')

#     return render(request,'aifit_app/login.html')

# def signup(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         try:
#             user = auth.create_user(email=email, password=password)
#             messages.success(request, "Sign-up successful!")
#             return redirect('login')
#         except Exception as e:
#             messages.error(request, "Sign-up failed. Please try again.")
#             return render(request,'aifit_app/signup.html')
        
#     return render(request,'aifit_app/login.html')

# def logout(request):
#     return render(request,'aifit_app/login.html')

def dashboard(request):
    return render(request,'aifit_app/dashboard.html')

def chat(request):
    print("User Id: ",request.user.id)
    return render(request,'aifit_app/chat.html')

def profile(request):
    # This command will get the user's id once the user is logged in
    # -> request.user.id <-
    return render(request,'aifit_app/profile.html')

def goals(request):
    # This command will get the user's id once the user is logged in
    # -> request.user.id <-
    return render(request,'aifit_app/goals.html')

def graph(request):
    # This command will get the user's id once the user is logged in
    # -> request.user.id <-
    return render(request,'aifit_app/graph.html')

# def previous_workouts(request):
#     # This command will get the user's id once the user is logged in
    # -> request.user.id <-
    #return render(request,'aifit_app/previousworkouts.html')

def line_chart(request):
    # This command will get the user's id once the user is logged in
    # -> request.user.id <-
    return render(request, 'aifit_app/graph.html')

def workout(request):
    # This command will get the user's id once the user is logged in
    # -> request.user.id <-
    return render(request, 'aifit_app/workouts.html')