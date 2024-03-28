from collections import Counter
from firebase_admin import firestore
from django.shortcuts import redirect
from aifit_app.forms import AddGoalForm

db = firestore.client()

def get_goal_lists():

    daily_goals = []
    weekly_goals = []
    longterm_goals = []

    docs = db.collection('goals').get()
    for doc in docs:
        goal_data = doc.to_dict()

        if goal_data['type'] == 'daily':
            daily_goals.append({
                'id': doc.id,
                'user_id': goal_data.get('user_id', ''),
                'type': goal_data.get('type', ''),
                'goal': goal_data.get('goal', ''),
                'is_completed': goal_data.get('is_completed', ''),
                'date_created': goal_data.get('date_created', ''),
                'when_completed': goal_data.get('when_completed', '')
            })
    
        elif goal_data['type'] == 'weekly':
            weekly_goals.append({
                'id': doc.id,
                'user_id': goal_data.get('user_id', ''),
                'type': goal_data.get('type', ''),
                'goal': goal_data.get('goal', ''),
                'is_completed': goal_data.get('is_completed', ''),
                'date_created': goal_data.get('date_created', ''),
                'when_completed': goal_data.get('when_completed', '')
            })

        elif goal_data['type'] == 'long-term':
            longterm_goals.append({
                'id': doc.id,
                'user_id': goal_data.get('user_id', ''),
                'type': goal_data.get('type', ''),
                'goal': goal_data.get('goal', ''),
                'is_completed': goal_data.get('is_completed', ''),
                'date_created': goal_data.get('date_created', ''),
                'when_completed': goal_data.get('when_completed', '')
            })
    
    return daily_goals, weekly_goals, longterm_goals

def add_goal(request):
    db = firestore.client()
    if request.method == "POST":
        form = AddGoalForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            goal_type = form.cleaned_data['type']  
            goal_ref = db.collection('goals').document()
            goal_data = {
                'user_id': request.user.id,  
                'type': goal_type,
                'goal': content,
                'is_completed': False, 
                'date_created': firestore.SERVER_TIMESTAMP
            }
            goal_ref.set(goal_data)
            return redirect('goals')
        
def update_goal_completion(request, goal_id):
   
    if request.method == 'POST':
        is_completed = request.POST.get('is_completed', 'false') == 'true'
        
        goal_ref = db.collection('goals').document(goal_id)
        goal_ref.update({'is_completed': is_completed})
        
        return redirect('goals')
