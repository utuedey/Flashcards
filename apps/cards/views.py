#!/usr/bin/python3

from django.views.generic import (
    ListView
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
