from __future__ import unicode_literals

# Third Party Stuff
from django import forms

# Carbon Stuff
from .models import Customer


class CustomerAdminForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ["id"]

    def __init__(self, *args, **kwargs):
        super(CustomerAdminForm, self).__init__(*args, **kwargs)
