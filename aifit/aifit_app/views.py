from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.template import loader

from .models import User, Workout
from .forms import SignUpForm, UserLoginForm

import firebase_admin
from firebase_admin import auth, firestore
from google.cloud.firestore_v1 import SERVER_TIMESTAMP

#FUNCTIONS
from .static.functions.functions import get_goals, get_todays_workout
from .static.functions.goals import update_goal_completion, add_goal, get_goal_lists
from fire.firebase import firebaseInit, Firebase
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

def chat(request):
    return render(request,'aifit_app/chat.html')

##################################################################################################################

##################################################################################################################
# (Name)

def profile(request):
    return render(request,'aifit_app/profile.html')

##################################################################################################################

##################################################################################################################
# Jennifer

def goals(request):

    daily_goals, weekly_goals, longterm_goals = get_goal_lists()

    return render(request,'aifit_app/goals.html', {
        'daily_goals': daily_goals,
        'weekly_goals': weekly_goals,
        'longterm_goals': longterm_goals
        }) 

##################################################################################################################


##################################################################################################################
# (Name)

class LineChartJSONView(View):
    user_id='hfIg3WidzBTHgezNF8O2'

    def get(self, request, *args, **kwargs):
        # This command will get the user's id once the user is logged in
        # -> request.user.id <-
        db = firestore.client()
        graph_data = db.collection('graph').where('user_id', '==', self.user_id).stream()
        print(graph_data)
        labels = []
        body_fat = []
        muscle_mass = []
        for data in graph_data:
            data_dict = data.to_dict()
            labels.append(data_dict['time_period'])
            body_fat.append(data_dict['body_percentage_fat'])
            muscle_mass.append(data_dict['muscle_mass_percentage'])
            #print(data_dict)

        print(body_fat)
        print(muscle_mass)

        data = {
            "type":'line',
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
line_chart_json = LineChartJSONView.as_view()

def line_chart(request):
    # This command will get the user's id once the user is logged in
    # -> request.user.id <-
    return render(request, 'aifit_app/graph.html')

def workout(request):
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
    return render(request, 'aifit_app/workouts.html', {'workouts': workouts})

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
