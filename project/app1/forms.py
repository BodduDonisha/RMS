from django import forms
from .models import Details

class RequestForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['Name', 'Phone', 'Email', 'Location', 'Message']
    