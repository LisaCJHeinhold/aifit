from django.urls import path
from . import views
from .views import line_chart, line_chart_json, workout

urlpatterns = [
    path('', views.home, name='home'),
    path('chart', views.line_chart, name='line_chart'),
    path('chartJSON', views.line_chart_json, name='line_chart_json'),
    path('graph', views.line_chart, name='line_chart'),
    path('workout', views.workout, name='workout'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('chat/', views.chat, name='chat'),
    path('profile/', views.profile, name='profile'),
    path('goals/', views.goals, name='goals'),
    path('previousworkouts/', views.previous_workouts, name='previous_workouts'),
]