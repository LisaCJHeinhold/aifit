from django.urls import path
from . import views
from .views import line_chart, line_chart_json, workout

urlpatterns = [
    path('', views.home, name='home'),
    path('chart', views.line_chart, name='line_chart'),
    path('chartJSON', views.line_chart_json, name='line_chart_json'),
    path('graph', views.line_chart, name='line_chart'),
    path('workout', views.workout, name='workout')
]