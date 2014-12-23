from django import forms


class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class SignupForm(forms.Form):
    email = forms.EmailField()
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirmation = forms.CharField(label='Confirm', widget=forms.PasswordInput())
