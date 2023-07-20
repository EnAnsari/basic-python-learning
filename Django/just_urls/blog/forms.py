from django import forms
from .models import Account


class AccountForm(forms.Form):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    first_name = forms.CharField(max_length=25, label='First Name')
    last_name = forms.CharField(max_length=50, label='Last Name')
    phone = forms.CharField(max_length=11, required=True, label='Phone Number')
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect, label='Gender')
    address = forms.CharField(max_length=250, widget=forms.Textarea, label='Address')
    age = forms.IntegerField(label='Age')

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone:
            if not phone.isnumeric():
                raise forms.ValidationError('phone number must be numeric!')
            else:
                return phone

    def clean_age(self):
        age = self.cleaned_data['age']
        if age:
            if age < 0:
                raise forms.ValidationError('age can not be negative!')
            else:
                return age
