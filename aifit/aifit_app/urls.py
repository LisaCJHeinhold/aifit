from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('chat/', views.chat, name='chat'),
    path('profile/', views.profile, name='profile'),
    path('goals/', views.goals, name='goals'),
    path('graph/', views.graph, name='graph'),
    path('previousworkouts/', views.previous_workouts, name='previous_workouts'),
    
    
]