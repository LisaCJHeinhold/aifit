import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore




# Create your views here.
def firebaseInit(): 
    # Use a service account.
    cred = credentials.Certificate('fire/aifit-42d60-4b74ea669715.json')
    if cred != None :
        print('credentials were read', cred)
        app = firebase_admin.initialize_app(cred)
        print('app was initialized', app)
        db = firestore.client()
        print('Firestor client', db)
    print('credentials were not read', cred)
        
    return

def firebaseAuth():
    return