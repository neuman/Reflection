from __future__ import unicode_literals

from django.db import models

from carteblanche.base import Verb, Noun
import django.contrib.auth

# Create your models here.

class Auditable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        try:
            return self.__unicode__()
        except Exception as e:
            return "auditable string goes here"

    class Meta:
        abstract = True

class TermSheet(Auditable):
    title = models.CharField(max_length=500, default="Unknown Title")
    terms = models.TextField(default='', null=True, blank=True)

    def __unicode__(self):
        try:
            return self.title
        except Exception as e:
            return "error parsing title"


class ConsentManager(models.Manager):
    def get_most_recent_timesheet(self):
        return TermSheet.objects.filter().order_by('-id')[0]

    def is_up_to_date(self, user):
        if Consent.objects.filter(user=user, termsheet=self.get_most_recent_timesheet()).count() > 0:
            return True
        else:
            return False


class Consent(Auditable):
    termsheet = models.ForeignKey(TermSheet, null=True, blank=True)
    user = models.ForeignKey(django.contrib.auth.models.User, null=True, blank=True, related_name="terms_consent")
    objects = ConsentManager()

    def __unicode__(self):
        try:
            return self.termsheet.title + " | " + self.user.email
        except Exception as e:
            return "error parsing title"
