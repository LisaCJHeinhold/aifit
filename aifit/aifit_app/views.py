from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'aifit_app/index.html')