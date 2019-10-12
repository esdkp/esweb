"""
DKP Forms
"""
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from .models import Raid


class RaidCreateForm(forms.ModelForm):
    """
    Raid Create Form
    """

    class Meta:
        model = Raid
        fields = ["date", "event", "attendance_value"]
        widgets = {"date": AdminDateWidget()}
