#!/usr/bin/env python3

from django import forms

class CardCheckForm(forms.Form):
    """A sublcass form that checks 
       if a users know the answer to a question.
    Fields:
    - card_id (Integer): primary key of the card the user is checking
    - solved (Boolean): Value set to True if user know the answer
                        and False if the user don't
    """
    card_id = forms.IntegerField(required=True)
    solved = forms.BooleanField(required=False)
