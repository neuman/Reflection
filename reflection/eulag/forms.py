from django import forms
from django.contrib.auth.models import User
import django.forms.extras.widgets as widgets

class BootstrapForm(forms.Form):
    exclude = ['changed_by']
    def __init__(self, *args, **kwargs):
        super(BootstrapForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if field.widget.attrs.has_key('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs.update({'class':'form-control'})

class ModelBootstrapForm(forms.ModelForm):
    exclude = ['changed_by']
    def __init__(self, *args, **kwargs):
        super(ModelBootstrapForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if field.widget.attrs.has_key('class'):
                field.widget.attrs['class'] += ' form-control'
            else:
                field.widget.attrs.update({'class':'form-control'})

class BooleanForm(forms.Form):
    decision = forms.BooleanField(required=True, label="Confirm", help_text="I swear, I'm ready to do this.")

    def clean(self):
        cleaned_data = super(BooleanForm, self).clean()
        decision = cleaned_data.get("decision")

        if decision==None:
            self._errors["decision"] = self.error_class(["You have to check the box if you want to publish."])
            # These fields are no longer valid. Remove them from the
            # cleaned data.


        # Always return the cleaned data, whether you have changed it or
        # not.
        return cleaned_data