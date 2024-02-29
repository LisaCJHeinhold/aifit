from django.urls import path
from . import views
from .views import line_chart, line_chart_json, workout

urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< HEAD
    # chart graph url
    path('chart', views.line_chart, name='line_chart'),
    path('chartJSON', views.line_chart_json, name='line_chart_json'),
<<<<<<< HEAD
    path('line_chart', views.line_chart, name='line_chart'),
    # other urls
=======
    path('graph', views.line_chart, name='line_chart'),
>>>>>>> d8d9c91 (views and gitignore)
    path('workout', views.workout, name='workout'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('chat/', views.chat, name='chat'),
    path('profile/', views.profile, name='profile'),
    path('goals/', views.goals, name='goals'),
<<<<<<< HEAD
    path('graph/', views.graph, name='graph'),
<<<<<<< HEAD
<<<<<<< HEAD
    path('previous_workouts/', views.previous_workouts, name='previous_workouts'),
    # path('display_first_name/', views.display_first_name, name='display_first_name'),
    # path('display_last_name/', views.display_last_name, name='display_last_name'),

=======
    path('previousworkouts/', views.previous_workouts, name='previousworkouts'),
>>>>>>> 00b6b73 (error fixes)
=======
    path('previous_workouts/', views.previous_workouts, name='previous_workouts'),
>>>>>>> b1b68f1 (Created a static file to keep javascript, css, and images inside. also created a template file to copy from to include in your html.)
    
    # allauth
    path('accounts/profile/', views.profile, name="profile"),
    
=======
    path('chart', views.line_chart, name='line_chart'),
    path('chartJSON', views.line_chart_json, name='line_chart_json'),
    path('graph', views.line_chart, name='line_chart'),
    path('workout', views.workout, name='workout')
>>>>>>> 749e940 (graph changes, and hecka stuff for workouts)
=======
    path('previousworkouts/', views.previous_workouts, name='previous_workouts'),
>>>>>>> d8d9c91 (views and gitignore)
]