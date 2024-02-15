from django.shortcuts import render
from fire.firebase import firebaseInit



# Create your views here.
def home(request):
    firebaseInit()
    return render(request, 'aifit_app/index.html')