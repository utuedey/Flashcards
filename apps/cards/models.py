#!/usr/bin/env python3

from django.db import models

NUM_OF_BOXES = 5 
BOXES = range(1, NUM_OF_BOXES + 1)

class Card(models.Model):
    """A table in my database with the following fields
    - question
    - answer
    - box
    - date_created
    """
    question = models.CharField(max_length=120)
    answer = models.CharField(max_length=120)
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    # Timestamp of the card's date and time of creation
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns  a string representation of the card objects"""
        return self.question

    def move(self, solved):
        """Method replicate the behavior of moving a card between boxes
        Argument:
        - solved (bool): True if the user knows the answer
                         False if the user doesn't know the answer
        """
        # Define new_box variable as the value of the box
        # depending on the argument value
        new_box = self.box + 1 if solved else BOXES[0]
        
        if new_box in BOXES:
            self.box = new_box
            self.save()
        return self