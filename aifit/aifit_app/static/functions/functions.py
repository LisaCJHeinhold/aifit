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

def get_todays_workout():
    current_date = datetime.today()
    
    day_of_week = current_date.strftime('%A')

    docs = db.collection('user_workouts').where('day_of_week', '==', day_of_week).get()
    
    for doc in docs:
        workout_data = doc.to_dict()
        return workout_data.get('day_schedule')
    
    return None 