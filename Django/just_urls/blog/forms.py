from django import forms
from .models import *


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


class ShareForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'name-class'}), required=True, label='Message')
    name = forms.CharField(widget=forms.TextInput, max_length=25, required=True, label='Full name')
    to = forms.EmailField(required=True, label='Email')


class MyFor(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'titleClass'
            })
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'body': forms.Textarea(attrs={'class': 'body-of-comment'})
        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(), label='old password')
    new_password1 = forms.CharField(widget=forms.PasswordInput(), label='new password')
    new_password2 = forms.CharField(widget=forms.PasswordInput(), label='repeat of new password')

    def clean_new_password1(self):
        new_password = self.cleaned_data.get('new_password1')
        if len(new_password) < 8:
            raise forms.ValidationError('Your Password must be 8 character minimum!')
        return new_password

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 != password2:
            raise forms.ValidationError('new password and its repeat isn\'t equal!')
        return password2
