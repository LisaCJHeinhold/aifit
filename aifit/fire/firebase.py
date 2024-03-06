import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



class Firebase:
    cred_path = 'fire/aifit-42d60-4b74ea669715.json'
   
   
    def __init__(self):
        self.cred = credentials.Certificate(self.cred_path)
        
        try:
            firebase_admin.get_app()
        except ValueError:
            firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()
        # firebase_admin.initialize_app(self.cred)
        # self.db = firestore.client()
        # print('__init__ was called')

    def get_data(self, collection, document):
        doc_ref = self.db.collection(collection).document(document)
        doc = doc_ref.get()  
        if doc.exists:
            return doc.to_dict()
        else:
            return None

    def set_data(self, collection, document, data):
        doc_ref = self.db.collection(collection).document(document)
        doc_ref.set(data)


# below is not need unless class doesn't work out
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