from django.shortcuts import render
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

# Create your views here.
def home(request):
    return render(request, 'aifit_app/index.html')

def line_chart(request):
    return render(request, 'aifit_app/graph.html')

def workout(request):
    return render(request, 'aifit_app/workouts.html')