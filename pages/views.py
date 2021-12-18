from django.views.generic import TemplateView, ListView
from cards.models import Card


class HomePageView(ListView):
    template_name = 'home.html'
    model = Card
    fields = ['title', 'image', 'summaryText']

class AboutPageView(TemplateView):
    template_name = 'about.html'


class LoginPageView(TemplateView):
    template_name = 'Registration/login.html'


class SignUpPageView(TemplateView):
    template_name = 'Registration/signup.html'


