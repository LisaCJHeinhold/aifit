from django.shortcuts import render, redirect
# from fire.firebase import firebaseInit, Firebase
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.template import loader
from .models import User, Workout
from .forms import SignUpForm, UserLoginForm
import firebase_admin
from firebase_admin import auth, firestore
from google.cloud.firestore_v1 import SERVER_TIMESTAMP
from .static.functions.functions import get_goals, get_todays_workout, get_num_of_exercises, get_time, get_todays_date, get_workout_ideas, get_body_fat, get_muscle_mass, get_weight, get_workout

from .static.functions.functions import get_goals, get_todays_workout, get_num_of_exercises, get_time, get_todays_date, get_workout_ideas
from .static.functions.open_ai import open_ai_conversation, log_conversation, ChatCompletionMessage, get_messages
from django.contrib.auth.decorators import login_required
import json
from datetime import datetime
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

import os
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import id_token
from google.auth.transport import requests
import jwt


def sign_in(request):
    return render(request, 'aifit_app/auth/sign_in.html')

@csrf_exempt
def auth_receiver(request):
    """
    Google calls this URL after the user has signed in with their Google account.
    """
    token = request.POST['credential']

    try:
        user_data = id_token.verify_oauth2_token(
            token, requests.Request(), os.environ['GOOGLE_OAUTH_CLIENT_ID']
        )
    except ValueError:
        return HttpResponse(status=403)

    # In a real app, I'd also save any new user here to the database. See below for a real example I wrote for Photon Designer.
    # You could also authenticate the user here using the details from Google (https://docs.djangoproject.com/en/4.2/topics/auth/default/#how-to-log-a-user-in)
    request.session['user_data'] = user_data

    return redirect('sign_in')


def sign_out(request):
    del request.session['user_data']
    return redirect('sign_in')


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

# def home(request):
#     # firebaseInit()
#     # Assuming the credentials file is located at 'path/to/your/credentials.json'
#     firebase_instance = Firebase()
#     print(firebase_instance)

#FUNCTIONS
from .static.functions.functions import get_goals, get_todays_workout
from .static.functions.goals import update_goal_completion, add_goal, delete_goal, get_goal_lists
# from fire.firebase import firebaseInit, Firebase
from django.views import View
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

# GRAPH FUNCTIONS
#import jsonresponse


##################################################################################################################
# (Name)
def dashboard(request):
    goals = get_goals()
    today_workout = get_todays_workout()
    return render(request,'aifit_app/dashboard.html', {'goals': goals, 'today_workout': today_workout})

##################################################################################################################


##################################################################################################################
# E 

def create_conversation(role, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "role": role,
        "message": message,
        "timestamp": timestamp
    }
    import json

def chat(request):
    # Get conversation data initially
    get_conversation = get_messages()
    print('get_conversation', get_conversation)
    if request.method == 'POST':
        print("Post button was clicked")
        action = request.POST.get('action')
        print('action', action)
        
        user_input = request.POST.get('user_input', '')
        print('user_input', user_input)
        
        # Get AI response using OpenAI conversation
        ai_response = open_ai_conversation(user_input)
        print('ai_response', ai_response)
        
        if ai_response is not None:
            # Log user input and AI response
            log_conversation("user", user_input)
            log_conversation("ai", ai_response)

            # Update conversation data
            get_conversation = get_messages()

            # Convert conversation data to JSON
            conversation_json = json.dumps(get_conversation)
            context = {
                'conversation_data': conversation_json,
                'conversation': get_conversation
            }

            # Return AI response as JSON
            return render(request, 'aifit_app/chat.html', context)
        else:
            # If AI response is invalid, return an error response
            return JsonResponse({'error': 'Invalid AI response'}, status=400)
    
    # If request method is not POST, render the template with initial conversation data
    conversation_json = json.dumps(get_conversation)
    context = {
        'conversation_data': conversation_json,
        'conversation': get_conversation
    }
    return render(request, 'aifit_app/chat.html', context)

# @login_required
# def chat(request):
#     get_conversation = get_messages()
#     # get_conversation = ''
    
#     if request.method == 'POST':
#         print("Post button was clicked")
#         action = request.POST.get('action')
#         print('action', action)
        
#         # if action == 'send_message':
#             # print("add_post button was clicked")
#             # target_user_id = user_id
#             # post_content = request.POST.get('comment')
#             # post_image_url = request.FILES.get('picture')
            
#             # return redirect('profile')
    
#         user_input = request.POST.get('user_input', '')
#         print('user_input', user_input)
#         # Get AI response using OpenAI conversation
#         ai_response = open_ai_conversation(user_input)
#         print('ai_response', ai_response)
#         # Check if AI response is valid
#         if ai_response is not None:
#             # Create a ChatCompletionMessage object
#             completion_message = ChatCompletionMessage(ai_response)

#             # Serialize the object to JSON using the custom method
#             json_data = completion_message.to_json()

#             # Log user input and AI response
#             log_conversation("user", user_input)
#             log_conversation("ai", json_data)
#             conversation_json = json.dumps(get_conversation)
#             context = {
#                 'conversation_data':conversation_json,
#                 'conversation': get_conversation
#             }
#             # Return AI response as JSON
#             return render(request,'aifit_app/chat.html', context)


#         else:
#             # If AI response is invalid, return an error response
#             return JsonResponse({'error': 'Invalid AI response'}, status=400)
    
    # conversation_data = [
    #     {"role": "user", "message": "Hello, how are you?", "timestamp": "2024-04-03 14:30:00"},
    #     {"role": "ai", "message": "I'm fine, thank you.", "timestamp": "2024-04-03 14:31:00"},
    #     {"role": "user", "message": "That's good to hear!", "timestamp": "2024-04-03 14:32:00"},
    #     {"role": "ai", "message": "How can I assist you today?", "timestamp": "2024-04-03 14:33:00"}
    # ]

#     # Convert conversation data to JSON
#     # conversation_json = json.dumps(conversation_data)
#     conversation_json = json.dumps(get_conversation)
#     context = {
#         'conversation_data': conversation_json,
#         'conversation': get_conversation
#     }
#     # If request method is not POST, render the template without context
#     return render(request,'aifit_app/chat.html', context)

#################################################
# Sofia - importing functions from functions.py #
#################################################
from .static.functions.functions import get_first_names, get_last_names, get_current_weights




def profile(request):
 
    first_names = get_first_names()
    last_names = get_last_names()
    current_weights = get_current_weights()


   
    context = {
        'first_names': first_names,
        'last_names': last_names,
        'current_weights': current_weights
    }


    return render(request, 'aifit_app/profile.html', context)






##################################################################################################################

##################################################################################################################
# Jennifer

def goals(request):

    daily_goals, weekly_goals, longterm_goals = get_goal_lists(request.user.id)

    return render(request,'aifit_app/goals.html', {
        'daily_goals': daily_goals,
        'weekly_goals': weekly_goals,
        'longterm_goals': longterm_goals
        }) 

##################################################################################################################


##################################################################################################################
# (Name)

# class LineChartJSONView(View):
#     user_id='hfIg3WidzBTHgezNF8O2'

#     def get(self, request, *args, **kwargs):
#         # This command will get the user's id once the user is logged in
#         # -> request.user.id <-
#         db = firestore.client()
#         graph_data = db.collection('graph').where('user_id', '==', self.user_id).stream()
#         print(graph_data)
#         labels = []
#         body_fat = []
#         muscle_mass = []
#         for data in graph_data:
#             data_dict = data.to_dict()
#             labels.append(data_dict['time_period'])
#             body_fat.append(data_dict['body_percentage_fat'])
#             muscle_mass.append(data_dict['muscle_mass_percentage'])
#             #print(data_dict)

#         print(body_fat)
#         print(muscle_mass)

#         data = {
#             "type":'line',
#             "labels": labels,
#             "datasets": [
#                 {
#                     "label": "% Body Fat",
#                     "data": body_fat,
#                     "borderColor": 'blue',
#                     "backgroundColor": 'rgba(0, 0, 255, 0.1)'
#                 },
#                 {
#                     "label": "% Muscle Mass",
#                     "data": muscle_mass,
#                     "borderColor": 'red',
#                     "backgroundColor": 'rgba(255, 0, 0, 0.1)'
#                 }
#             ]
#         }

#         return JsonResponse(data)
def graph(request):
    return render(request,'aifit_app/graph.html')

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
# line_chart_json = LineChartJSONView.as_view()
# def home(request):
#     # firebaseInit()
#     # Assuming the credentials file is located at 'path/to/your/credentials.json'
#     firebase_instance = Firebase()
#     print(firebase_instance)
#      # Now you can use the firebase_instance to interact with Firebase services
#     data = firebase_instance.get_data(collection='your_collection', document='your_document')
#     print(data)
    
#     return render(request, 'aifit_app/dashboard.html')

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
    goals = get_goals()
    today_workout = get_todays_workout()
    day = get_todays_date()
    time = get_time() 
    workout_ideas = get_workout_ideas()
    number_of_workouts = get_num_of_exercises()
    body_fat = get_body_fat()
    muscle_mass = get_muscle_mass()
    weight = get_weight()
    workout = get_workout()
    
    return render(request,'aifit_app/dashboard.html', {'goals': goals, 'today_workout': today_workout, 'day': day, 'time': time, 'workout_ideas': workout_ideas, 'num_of_workouts': number_of_workouts, 'body_fat': body_fat, 'muscle_mass': muscle_mass, 'weight': weight, 'workout': workout})


def profile(request):
    return render(request,'aifit_app/profile.html')

def graph(request):
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
   # user =  request.user.id
   # user_workouts = get_user_workouts(request)
   # user_exercises = get_user_exercises(request)
   user = "jhghjgjgjhgghjghjjkh"
   action = request.POST.get('action')
   
   print('action',action)
   if action == 'create_exercise':
       print('create_exercise')
       exercise_name = request.POST.get('exercise_name')
       exercise_sets = request.POST.get('goal_sets')
       exercise_reps = request.POST.get('goal_reps')
       exercise_weight = request.POST.get('goal_weight')
       exercise_best = request.POST.get('exercise_best')
       order = request.POST.get('order')

       db = firestore.client()
       workout_ref = db.collection('user_exercises')
       workout_ref.add({
           'user_workout_id': user,
           'exercise_name': exercise_name,
           'goal_sets': exercise_sets,
           'goal_reps': exercise_reps,
           'goal_weight': exercise_weight,
           'best_weight': exercise_best,
           'order': order,
           'date_created': SERVER_TIMESTAMP
       })
       return redirect('workout')
   elif action == 'create_workout':
       print('create_workout')
       workout_type = request.POST.get('workout_type')
       workout_time = request.POST.get('workout_time')
       workout_exercises = request.POST.get('workout_exercises')

       db = firestore.client()
       workout_ref = db.collection('user_workouts')
       workout_ref.add({
           'user_id': user,
           'type': workout_type,
           'time': workout_time,
           'number_exercises': workout_exercises,
           'date_created': SERVER_TIMESTAMP
       })
       return redirect('workout')
   

   user_workouts = firestore.client().collection('user_workouts').stream()
   workouts = []
   for workout in user_workouts:
       workouts_data = workout.to_dict()
       workouts.append({
           'user_id': workouts_data.get('user_id', ''),
           'type': workouts_data.get('type', ''),
           'time': workouts_data.get('time', ''),
           'date_created': workouts_data.get('date_created', ''),
           'number_exercises': workouts_data.get('number_exercises', ''),
       })
   
   db = firestore.client()
   user_exercises = db.collection('user_exercises').stream()
   exercises = []
   for exercise in user_exercises:
       exercise_data = exercise.to_dict()
       print(exercise_data)
       exercises.append({
           'goal_reps': exercise_data.get('goal_reps', ''),
           'goal_sets': exercise_data.get('goal_sets', ''),
           'order': exercise_data.get('order', ''),
           'type_of_exercise': exercise_data.get('type_of_exercise', ''),
           'exercise_name': exercise_data.get('exercise_name', ''),
           'best_weight': exercise_data.get('best_weight', ''),
           'goal_weight': exercise_data.get('goal_weight', ''),
       })
   

   completed_workout = firestore.client().collection('completed_workout').stream()
   completed_workouts = []
   for workout in completed_workout:
       workout_data = workout.to_dict()
       print(workout_data)
       completed_workouts.append({
           'day_completed': workout_data.get('day_completed', ''),
           'exercises': workout_data.get('exercises', ''),
           'type': workout_data.get('type', ''),
       })
   context = {
       'workouts': workouts,
       'exercises': exercises,
       'completed_workouts': completed_workouts
   
   }
       # print(workouts_data.get('type', '')) 
       # print(workouts_data.get('number_exercises', ''))
   return render(request, 'aifit_app/workouts.html', context)   

#def previous_workouts(request):
#     # This command will get the user's id once the user is logged in
    # -> request.user.id <-
    #return render(request,'aifit_app/previousworkouts.html')

##################################################################################################################




##################################################################################################################
# (Name)

##################################################################################################################



##################################################################################################################
# (Name)

##################################################################################################################
