from django.views.decorators import csrf as csrf_decorators
from django.views.generic.base import TemplateView


class Helloworld(TemplateView):
    template_name = 'helloworld.html'

    @csrf_decorators.csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(Helloworld, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)        
