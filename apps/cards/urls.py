from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="cards/index.html"),   # url for the landing_page
          name="home"
          ),
    path(
        "cards",
        views.CardListView.as_view(),
        name="card-list"
    ),
]
