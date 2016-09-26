from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.core.urlresolvers import reverse


import eulag.models as em

# Create your views here.
class SignView(CreateView):
    template_name = settings.EULAG_EULA_TEMPLATE
    model = em.Consent
    fields = []

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(SignView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['termsheet'] = em.Consent.objects.get_most_recent_timesheet()
        return context

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            if em.Consent.objects.is_up_to_date(self.request.user):
                return HttpResponseRedirect(settings.EULAG_UP_TO_DATE_REDIRECT)
        response = super(SignView, self).dispatch(*args, **kwargs)
        return response

    def get_success_url(self):
        self.object.user =self.request.user
        self.object.termsheet = em.Consent.objects.get_most_recent_timesheet()
        self.object.save()
        url = settings.EULAG_UP_TO_DATE_REDIRECT
        return url