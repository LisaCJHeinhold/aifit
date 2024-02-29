from django.shortcuts import render, redirect
from fire.firebase import firebaseInit, Firebase
from django.contrib import auth
from fire.firebase_auth import verify_id_token
from django.conf import settings
from django.http import JsonResponse
import firebase_admin
from firebase_admin import auth


# def login(request):
#     firebase_config = settings.FIREBASE_CONFIG
#     if request.method == 'POST':
#         id_token = request.POST.get('id_token')
#         user = verify_id_token(id_token)
#         if user:
#             auth.login(request, user)
#             return redirect('dashboard')  # Redirect to dashboard page after login
#         else:
#             # Handle invalid login
#             pass
#     return render(request, 'aifit_app/login.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if email is None or password is None:
            return JsonResponse({"error": "Email or password is missing"}, status=400)

        try:
            user = auth.get_user_by_email(email)
            # Firebase user exists, try to sign in
            user = auth.sign_in_with_email_and_password(email, password)
            # Authentication successful, return user's Firebase UID
            return JsonResponse({"uid": user["localId"]})
        except firebase_admin.auth.UserNotFoundError:
            # Firebase user doesn't exist
            return JsonResponse({"error": "User not found"}, status==400)
    
    return render(request, "aifit_app/login.html")

def signup(request):
    # Implement signup logic here
    pass

def logout(request):
    auth.logout(request)
    return redirect('login')

from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May"]

    def get_providers(self):
        """Return names of datasets."""
        return ["% Body Fat", "% Muscle Mass"]

    def get_data(self):
        """Return 2 datasets to plot."""

        return [[28, 27 , 24, 23, 23, 20, 20],
                [12, 13, 15, 15, 17, 16, 17]]


line_chart = TemplateView.as_view(template_name='graph.html')
line_chart_json = LineChartJSONView.as_view()
def home(request):
    # firebaseInit()
    # Assuming the credentials file is located at 'path/to/your/credentials.json'
    firebase_instance = Firebase()
    print(firebase_instance)
    
     # Now you can use the firebase_instance to interact with Firebase services
    data = firebase_instance.get_data(collection='your_collection', document='your_document')
    print(data)
    
    return render(request, 'aifit_app/index.html')

def dashboard(request):
    return render(request,'aifit_app/dashboard.html')

def chat(request):
    return render(request,'aifit_app/chat.html')

def profile(request):
    return render(request,'aifit_app/profile.html')

def goals(request):
    return render(request,'aifit_app/goals.html')

def graph(request):
    return render(request,'aifit_app/graph.html')

def previous_workouts(request):
    return render(request,'aifit_app/previousworkouts.html')

def line_chart(request):
    return render(request, 'aifit_app/graph.html')

def workout(request):
    return render(request, 'aifit_app/workouts.html')