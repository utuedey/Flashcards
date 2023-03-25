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
