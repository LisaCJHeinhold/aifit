# BOSTON IS WORKING WITH THIS
from django.shortcuts import render
from firebase_admin import credentials, firestore
from datetime import datetime 

db = firestore.client()

def get_goals():
    goals = []
    docs = db.collection('goals').get()
    for doc in docs:
        goals_dictionary = doc.to_dict()
        goals.append(goals_dictionary['goal'])
    return goals

def get_graph():
    pass

<<<<<<< Updated upstream
def get_todays_date():
=======
def get_day_of_week():
>>>>>>> Stashed changes
    current_date = datetime.today()
    day_of_week = current_date.strftime('%A')
    return day_of_week

<<<<<<< Updated upstream
    return day_of_week

def get_todays_workout():
    docs = db.collection('user_workouts').get()
    today = get_todays_date()

=======
def get_todays_workout():
    
    docs = db.collection('user_workouts').where('day_of_week', '==', get_day_of_week()).get()
    
>>>>>>> Stashed changes
    for doc in docs:
        workout_data = doc.to_dict()
        if workout_data['day_schedule'] == today:
            return workout_data.get('type')
    return "error"

def get_time():
    docs = db.collection('user_workouts').get()
    today = get_todays_date()

    for doc in docs:
        workout_data = doc.to_dict()
        if workout_data['day_schedule'] == today:
            return workout_data['time']
    return "error"

def get_num_of_exercises():
    docs = db.collection('user_workouts').get()
    today = get_todays_date()

    for doc in docs:
        workout_data = doc.to_dict()
        if workout_data['day_schedule'] == today:
            return workout_data['number_exercises']
    return "error"

def get_workout_ideas():
    docs = db.collection('user_workouts').get()
    today = get_todays_date()

    for doc in docs:
        workout_data = doc.to_dict()
        if workout_data['day_schedule'] == today:
            return workout_data['workout_ideas']
    return "error"