# Flashcards

![Landing_page](https://github.com/utuedey/Tutorial_images/blob/main/Tutorials/landing_page.png?raw=true)

# Introduction
Flashcards app is a full-stack web-application that is designed to help students learn by studying with digital flashcards.
(A flashcard is a card bearing information on both sides, which is intended to be use as an aid memorization).
The user can easily create their own sets of flashcards with the easy-to-use interface of the application

## The Context
This project is my Portfolio Project, concluding my Foundation Year at Alx School. We were able to choose who we wanted to work with and what we wanted to work on, as long as we present a working program at the end of the three weeks of development.

# Project Overview
The Django Flashcards app replicates a spaced repetition system which can boost one's learning ability.
- You have Five boxes that can contain Flashcards.
- when you create a flashcard, you put it into the first box.
- To test your knowledge, you choose a box, pick a random flashcard, and check if you know the answer to the card's question.
- If you know the answer, then you move the card to the next higher box.
- If you don't know the answer, then you move the card back to the first box.
- The higher the box number, the less frequently you check the flashcard.

# Features
- Create a New card
- Edit an existing card
- List All created cards
- Move card to a new box

# Getting started
- User visits flashcards.tech
- click on the start app button on the landing page
- The app load the card_page
on the card_page you'll see all the existing cards and be able to create new ones.

![card_page](https://github.com/utuedey/Tutorial_images/blob/main/Tutorials/list_card_page.png?raw=true)

on each flashcards you can add a question and answer which you can later edit

![create_card_page](https://github.com/utuedey/Tutorial_images/blob/main/Tutorials/create_card.png?raw=true)

you can edit your existing cards on the edit_card page

![edit_card_page](https://github.com/utuedey/Tutorial_images/blob/main/Tutorials/edit_card.png?raw=true)

when you want to test your knowledge, you can navigate to a box to review the cards that the box contains.

![box_page](https://github.com/utuedey/Tutorial_images/blob/main/Tutorials/box_page.png?raw=true)

once you have learned the answer to the card's question, the card moves to the next box. If a flashcard move to 
the next box, that doesn't mean you're done with it. You'll still review it periodically to refresh your memory,
and it'll continue progressing through the boxes. Basically the higher the box number, the more likely that you
have mastered those concepts. If you don't know the answer to a card's question, then the card moves to the first box.

# Framework Architecture 
Django MVT

![Django_mvt](https://github.com/utuedey/Tutorial_images/blob/main/Tutorials/Django(MVT).png?raw=true)

- Model: It is the logical data structure behind the entire application
and is represented by a database.

- View: The View is the user interface — what you see in your browser when you render a website. 
It is represented by HTML/CSS/Javascript and Jinja files

- Template: A template consists of static parts of the desired HTML output 
as well as some special syntax describing how dynamic content will be inserted.

                                                                                                                        
# Authors
- Joseph A Utuedeye <https://github.com/utuedey>

I'm a backend software engineer and a student training to be chemical engineer
I worked on both the front-end and back-end of this project with help from Realpythons tutorials.

# Acknowledgments
- Alx school Mentors and fellow peers
- RealPython tutorials <realpython.com>

