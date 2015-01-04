from django import http
from django.contrib import auth
from django.contrib.auth import models as auth_models
from django.views.decorators import csrf as csrf_decorators
from django.views.generic import base as base_views
from django.views.generic import detail as detail_views
from django.views.generic import edit as edit_views
from django.views.generic import list as list_views
import forms
import models


class Helloworld(base_views.TemplateView):
    template_name = 'helloworld.html'

    @csrf_decorators.csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(Helloworld, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)        


class Home(list_views.ListView):
    template_name = 'index.html'
    model = models.Question
    paginate_by = 10

    def get_queryset(self):
        queryset = super(Home, self).get_queryset()
        queryset = queryset.select_related()
        if self.request.GET.get('by_rating'):
            queryset = queryset.order_by('-author__rating')
        else:            
            queryset = queryset.order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['by_rating'] = self.request.GET.get('by_rating', '')
        return context


class Signup(edit_views.FormView):
    template_name = 'signup.html'
    form_class = forms.SignupForm
    success_url = '/'

    def form_valid(self, form):
        auth_user = auth_models.User.objects.create_user(form.cleaned_data['login'], form.cleaned_data['email'], form.cleaned_data['password'])
        user = models.User(
            rating=0,
            user=auth_user,
        )
        user.save()
        auth_user = auth.authenticate(username=form.cleaned_data['login'], password=form.cleaned_data['password'])
        auth.login(self.request, auth_user)
        return http.HttpResponseRedirect(self.get_success_url())


class Question(detail_views.SingleObjectMixin, list_views.ListView):
    template_name = 'question.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=models.Question.objects.all())
        return super(Question, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.responses.order_by('-created').all()

    def post(self, request, pk):
        if not request.user.is_authenticated():
            return http.HttpResponse(status=401)
        text = request.POST.get('answer')
        if not text:
            return http.HttpResponseBadRequest()
        try:
            question = models.Question.objects.get(pk=pk)
        except models.Question.DoesNotExist:
            return http.HttpResponseNotFound()
        response = models.Response(
            text=text,
            question=question,
            author=request.user.ask_user,
            is_right=False,
        )
        response.save()
        return http.HttpResponse()


class Questions(list_views.ListView):
    queryset = models.Question.search
    template_name = 'questions.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(Questions, self).get_context_data(**kwargs)
        context['by_rating'] = self.request.GET.get('by_rating', '')
        context['query'] = self.request.REQUEST.get('q', '')
        return context

    def get_queryset(self):
        queryset = super(Questions, self).get_queryset()
        return queryset.query(self.request.REQUEST.get('q', ''))
