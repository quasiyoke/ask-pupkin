from django import forms
from django.utils import safestring, html, encoding
from django.forms import widgets
from django.contrib.auth import models as auth_models
import models

class ImageInput(forms.ClearableFileInput):
    template_with_initial = '%(initial_text)s %(initial)s %(clear_template)s%(input_text)s: %(input)s'

    def render(self, name, value, attrs=None):
        substitutions = {
            #uncomment to get 'Currently'
            'initial_text': "", # self.initial_text, 
            'input_text': self.input_text,
            'clear_template': '',
            'clear_checkbox_label': self.clear_checkbox_label,
            }
        template = '%(input)s'
        substitutions['input'] = widgets.Input.render(self, name, value, attrs)

        if value and hasattr(value, "url"):
            template = self.template_with_initial
            substitutions['initial'] = ('<img class="userpic userpic_input" src="%s" alt="%s"/>'
                                        % (html.escape(value.url),
                                           html.escape(encoding.force_unicode(value))))
            if not self.is_required:
                checkbox_name = self.clear_checkbox_name(name)
                checkbox_id = self.clear_checkbox_id(checkbox_name)
                substitutions['clear_checkbox_name'] = html.conditional_escape(checkbox_name)
                substitutions['clear_checkbox_id'] = html.conditional_escape(checkbox_id)
                substitutions['clear'] = forms.CheckboxInput().render(checkbox_name, False, attrs={'id': checkbox_id})
                substitutions['clear_template'] = self.template_with_clear % substitutions

        return safestring.mark_safe(template % substitutions)


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['avatar', ]

    avatar = forms.ImageField(widget=ImageInput())


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
