import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#sofia: import the render method for django:
from django.shortcuts import render


# cred = credentials.Certificate("fire/aifit-42d60-4b74ea669715.json")
# firebase_admin.initialize_app(cred)

db = firestore.client()

def get_goals(): 
    docs = db.collection('goals').get()
    for doc in docs:
        goals_dictionary = doc.to_dict()
        print(goals_dictionary['goal'])

# sofia: get first name from the database
def display_first_name(request):
    first_name = []
    docs = db.collection('profiles').get()
    for doc in docs:
        profile_data = doc.to_dict()
        if 'first_name' in profle_data:
            first_name.append(profile_data['first_name'])
    
    # Pass first name to the  html
    return render(request, '/templates/profile.html', {'first name': first_name})

def display_last_name(request):
    last_name = []
    docs = db.collection('profiles').get()
    for doc in docs:
        profile_data = doc.to_dict()
        if 'last_name' in profile_data:
            last_name.append(profile_data['last_name'])
    
    # Pass last name to the  html
    return render(request, '/templates/profile.html', {'last name': last_name})


# Sofia : get profiles info from firebase
def get_first_name():
    first_name = []
    docs = db.collection('profiles').get()
    for doc in docs:
        fname_dictionary = doc.to_dict()
        first_name.append(fname_dictionary['first_name'])
        
    return first_name

def get_last_name():
    last_name = []
    docs = db.collection('profiles').get()
    for doc in docs:
        lname_dictionary = doc.to_dict()
        last_name.append(lname_dictionary['last_name'])
        
    return last_name

