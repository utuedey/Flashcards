#!/usr/bin/python3

from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)
from .models import Card

class CardListView(ListView):
    """A class-based view that lists all the cards
    Attributes:
    - model: the model to work with
    - queryset: list of cards to display from the database
    """
    model = Card
    queryset = Card.objects.all().order_by("box", "-date_created")

class CardCreateView(CreateView):
    """A class-based view that creates a new card
    Attributes:
    - field: The fields the form would show
           - question field
           - answer field
           - box field
    - success_url: The url to return request to when the form is sent.
    """
    model = Card
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("card-create")

class CardUpdateView(CardCreateView, UpdateView):
    """A class-based view that inherits from CardCreateView and
    UpdateView that update an exisitng card.
    Attribute:
    -success_url: The url to return request to when the form is sent
    """
    success_url = reverse_lazy("card-list")
