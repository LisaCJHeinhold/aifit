from django.shortcuts import render
# from fire.firebase import firebaseInit, Firebase
from fire.firebase import Firebase


# Create your views here.
def home(request):
    # firebaseInit()
    # Assuming the credentials file is located at 'path/to/your/credentials.json'
    firebase_instance = Firebase()
    print(firebase_instance)
    
     # Now you can use the firebase_instance to interact with Firebase services
    data = firebase_instance.get_data(collection='your_collection', document='your_document')
    print(data)
    
    return render(request, 'aifit_app/index.html')