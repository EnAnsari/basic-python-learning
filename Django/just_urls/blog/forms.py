from django import forms
from .models import Account


class AccountForm(forms.Form):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=50)
    # phone = forms.CharField(max_length=11, null=True, blank=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    address = forms.CharField(max_length=250, widget=forms.Textarea)
