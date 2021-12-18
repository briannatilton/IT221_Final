from django.views.generic import ListView, DetailView
from .models import Card


class CardListView(ListView):
    model = Card
    template_name = 'listCards.html'
    fields = ['image', 'title', 'summaryText']

class CardDetailView(DetailView):
    model = Card
    template_name = 'card_detail.html'
    fields = ['title', 'author', 'ingredientsForRecipe', 'directionsForRecipe']