#!/usr/bin/python3

import random
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)
from django.shortcuts import get_object_or_404, redirect
from .models import Card
from .forms import CardCheckForm

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

class BoxView(CardListView):
    """A subclass of CardListView that lists the boxes.
    Attributes:
    template_name: The template that BoxView will render.
    
    """
    template_name = "cards/box.html"
    form_class = CardCheckForm

    def get_queryset(self):
        """Returns only the cards where the box number matches the box_num value."""
        return Card.objects.filter(box=self.kwargs["box_num"])
    
    def get_context_data(self, **kwargs):
        """Returns a dictionary with the number of boxes
        Argument:
        - Kwargs: = box_num
        """
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context
    
    def post(self, request, *args, **kwargs):
        """Handle incoming POST request of the cardcheckform"""
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            card.move(form.cleaned_data["solved"])

        return redirect(request.META.get("HTTP_REFERER"))

