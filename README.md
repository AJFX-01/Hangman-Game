# CS50P: HANGMAN & GUESSING GAME
#### Video Demo:  <https://youtu.be/_iriu-XjtWQ>
# Description:
The hangman is guessing in which the plyaer or user is prompt for a character , if the character is correct the character get one point added to there score and 2 chnaces added to their chnaces. if the player get the chracter wrong the point is deduct from thier chances.
the word guessed right are shown on the screen and the ones yet to guesed right are represnted by *, the word already guesed are also shown on the screen, if entered again, it will tell the user that the word has being guesed already.
 the three main important component of the game are:
# Chances:
the player get a total of 10 chances to get all the character right, if got wrong the chnaces will be reduced by one, if the guess is right they get two point added
# Scores:
if the player the guess right 1 point will be added to their score. if wrong, nothing will happen to scores.
# Level:
if the player get over one in scores and over 5 chances left, after all the suggestion they will get awarded the meduim level. if they get over 5 in score and over 10 in chances they will get high level award but if score and chances equal they will get low level award
# Word to predicted:
it is gotten from a list contaning over 100000 words english words which are choosen at random all the time
# Suggestions:
the suggestions kicks in ones the player has gotten over half of the length of word and chances left are high than five, the lettter suggested are predicted at random.
# Tests:
Pytest and unittest were carried out on three function in the program and all test was passed.
# Files:
the file here include:
### project.py
this contain the code for the main program and all the functions
### requirement.txt
this contains all the libraries installed
### test_project.py
this contains all the test function carried out on the program
### wordx,py
this contains list of the all the word selected from random

### improvements
gives the user the chance to play more than onces and then the overall score

    TODO