from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView, RedirectView

from sitegate.decorators import redirect_signedin, sitegate_view

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.list import ListView
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic import DetailView
from django.contrib.auth.models import User
from carteblanche.mixins import NounView
from django.contrib.auth import authenticate, login

import hello.models as cm

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/hello/entrance')
    return render(request, 'index.html')


@sitegate_view(widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3', redirect_to='/eula/sign/')  # This also prevents logged in users from accessing our sign in/sign up page.
def entrance(request):
    return render(request, 'pages/entrance.html', {'title': 'Sign in & Sign up'})

class GuideView(TemplateView):
    template_name = 'pages/guide.html'

class SelfAnalysisView(TemplateView):
    template_name = 'pages/selfanalysis.html'








class IndexView(RedirectView):

    def get_redirect_url(self, **kwargs):
        if self.request.user.is_authenticated():
            return '/hello/dashboard/'
        else:
            return '/hello/entrance/'

class DashboardView(TemplateView):
    template_name = 'index.html'