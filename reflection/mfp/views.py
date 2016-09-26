from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
import core.models as cm

# Create your views here.
class VisView(TemplateView):
    template_name = 'vis.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(VisView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        horizon = cm.get_time_horizon(3)
        dataPoints = cm.DataPoint.objects.filter(date__gte=horizon).order_by('date')
        dates = []
        calories = []
        sodium = []
        carbohydrates = []
        fat = []
        sugar = []
        protein = []
        for d in dataPoints:
            dates.append(str(d.date.month)+"/"+str(d.date.day)+"/"+str(d.date.year))
            calories.append(cm.calc_percent_of(d.datum['totals']['calories'], d.datum['goals']['calories']))
            sodium.append(cm.calc_percent_of(d.datum['totals']['sodium'], d.datum['goals']['sodium']))
            carbohydrates.append(cm.calc_percent_of(d.datum['totals']['carbohydrates'], d.datum['goals']['carbohydrates']))
            fat.append(cm.calc_percent_of(d.datum['totals']['fat'], d.datum['goals']['fat']))
            sugar.append(cm.calc_percent_of(d.datum['totals']['sugar'], d.datum['goals']['sugar']))
            protein.append(cm.calc_percent_of(d.datum['totals']['protein'], d.datum['goals']['protein']))

        context['calories'] = calories
        context['sodium'] = sodium
        context['carbohydrates'] = carbohydrates
        context['fat'] = fat
        context['sugar'] = sugar
        context['protein'] = protein
        context['dates'] = dates
        return context

