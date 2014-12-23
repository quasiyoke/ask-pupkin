from django.views.decorators import csrf as csrf_decorators
from django.views.generic import base as base_views
from django.views.generic import edit as edit_views
import forms


class Helloworld(base_views.TemplateView):
    template_name = 'helloworld.html'

    @csrf_decorators.csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(Helloworld, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)        


class Home(base_views.TemplateView):
    template_name = 'index.html'


class Login(edit_views.FormView):
    template_name = 'login.html'
    form_class = forms.LoginForm


class Signup(edit_views.FormView):
    template_name = 'signup.html'
    form_class = forms.SignupForm
