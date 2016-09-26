from django.conf import settings
from django.contrib import admin
import eulag.models

admin.site.register(eulag.models.TermSheet)
admin.site.register(eulag.models.Consent)