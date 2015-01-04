from django import forms
from django.contrib.auth import models as auth_models
import models


class QuestionForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(label='', widget=forms.Textarea())
    tags = forms.CharField()


class SignupForm(forms.Form):
    email = forms.EmailField()
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirmation = forms.CharField(label='Confirm', widget=forms.PasswordInput())

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            auth_models.User.objects.get(email=email)
        except auth_models.User.DoesNotExist:
            pass
        else:
            raise forms.ValidationError('There\'s already user with such email.')
        return email

    def clean_login(self):
        login = self.cleaned_data['login']
        try:
            auth_models.User.objects.get(username=login)
        except auth_models.User.DoesNotExist:
            pass
        else:
            raise forms.ValidationError('There\'s already user with such login.')
        return login

    def clean_password_confirmation(self):
        password_confirmation = self.cleaned_data['password_confirmation']
        if self.cleaned_data['password'] != password_confirmation:
            raise forms.ValidationError('Passwords dont match.')
        return password_confirmation
