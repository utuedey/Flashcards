#!/usr/bin/env python3

from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # Url route for the landing page
    path("", TemplateView.as_view(template_name="cards/index.html"),
          name="home"
          ),
    # Url route for the card list page
    path(
        "cards",
        views.CardListView.as_view(),
        name="card-list"
    ),
    # Url route for the card create page
    path(
        "new",
        views.CardCreateView.as_view(),
        name="card-create"
    ),
    # Url route for the card update page
    path(
        "edit/<int:pk>",
        views.CardUpdateView.as_view(),
        name="card-update"
    ),
    # Url route for the box page
    path(
        "box/<int:box_num>",
        views.BoxView.as_view(),
        name = 'box'
    ),
]
