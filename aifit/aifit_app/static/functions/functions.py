import firebase_admin
from firebase_admin import firestore, credentials

# cred = credentials.Certificate("/Users/bostonwilliams/Desktop/GitHub/aifit/aifit/fire/aifit-42d60-4b74ea669715.json")
# firebase_admin.initialize_app(cred)

db = firestore.client()

def get_goals(): 
    docs = db.collection('goals').get()
    for doc in docs:
        goals_dictionary = doc.to_dict()
        print(goals_dictionary['goal'])
