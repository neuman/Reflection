from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView

# Create your views here.
class VisView(TemplateView):
    template_name = 'vis.html'