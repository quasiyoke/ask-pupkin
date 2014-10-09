from django.views.generic.base import TemplateView


class Helloworld(TemplateView):
    template_name = 'helloworld.html'
