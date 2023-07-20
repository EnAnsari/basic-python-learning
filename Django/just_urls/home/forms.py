from django import forms


class ContactUsForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, required=True, label='Message')
    name = forms.CharField(max_length=25, required=True, label='Full name')
    email = forms.EmailField(required=True, label='Email')
    subject = forms.CharField(max_length=25, required=True, label='Subject')
    phone = forms.CharField(max_length=11, required=False, label='Phone Number')
