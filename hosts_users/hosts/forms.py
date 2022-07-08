from django import forms

from .models import Hosts


class HostsForm(forms.ModelForm):
    class Meta:
        model = Hosts
        fields = ('ip', 'port', 'resource', 'owner')
