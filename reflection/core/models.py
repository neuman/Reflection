from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User


# Create your models here.
class Auditable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        try:
            return self.__unicode__()
        except Exception as e:
            return "auditable string goes here"

    def get_parents(self):
        parents = [self]
        try:
            parents = parents + self.get_parent().get_parents()
        except Exception as e:
            parents.append(self.get_parent())
            return parents
        return parents

    def get_model_name(self):
        return self._meta.model_name

    class Meta:
        abstract = True


class DataPoint(Auditable):
    schemaless = JSONField(null=True, blank=True)