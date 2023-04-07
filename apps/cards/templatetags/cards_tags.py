#!/usr/bin/env python3

from django import template

from apps.cards.models import BOXES, Card

# Instance of library for registering template tags
register = template.Library()

# Tells Django that boxes_as_links is an inclusion link
@register.inclusion_tag("cards/box_links.html")
def boxes_as_links():
    """Returns a dictionary with the boxes data"""
    boxes = []
    for box_num in BOXES:
        # Keep track of the number of cards in the current box
        card_count = Card.objects.filter(box=box_num).count()
        boxes.append({
            "number": box_num,
            "card_count": card_count,
        })
    
    return {"boxes": boxes}
