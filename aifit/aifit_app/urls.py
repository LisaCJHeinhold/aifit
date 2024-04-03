from django.urls import path
from . import views
# from .views import line_chart, line_chart_json, workout

urlpatterns = [
    path('', views.dashboard, name='home'),
    
    path('sign-in', views.sign_in, name='sign_in'),
    path('sign-out', views.sign_out, name='sign_out'),
    path('auth-receiver', views.auth_receiver, name='auth_receiver'),
    
    # chart graph url
    path('chart', views.line_chart, name='line_chart'),
    # path('chartJSON', views.line_chart_json, name='line_chart_json'),
    path('line_chart', views.line_chart, name='line_chart'),
    # other urls
    path('workout', views.workout, name='workout'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('accounts/signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('chat/', views.chat, name='chat'),
    path('profile/', views.profile, name='profile'),
    
    path('goals/', views.goals, name='goals'),
    path('goals/add_goal/', views.add_goal, name='add_goal'),
    path('goals/update_goal/<str:goal_id>/', views.update_goal_completion, name='update_goal_completion'),
    path('graph/', views.graph, name='graph'),
    path('previous_workouts/', views.previous_workouts, name='previous_workouts'),
    
    # allauth
    path('accounts/profile/', views.profile, name="profile"),
    
    
]