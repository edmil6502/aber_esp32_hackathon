'''
Ideas:
    - Question comes up
    - Press button to flip flashcard
    - Rank wrong, right and easy
    - Skip button?
    - Store difficulty ranking to determine when that flashcard next appears
Sorting system?
    - Different "groups" for different topics of flashcards
    - Can filter by group to focus on one topic
    - Naming flashcards?
Navigating and writing flashcards:
    - Option to import from sd card/usb?
    - Can write mathematical notation
    - Keyboard onscreen? (if battery powered so can add flashcards on the go (experiment with unplugging and see if it saves))
    - Some kind of menu with a search feature (flashcard "groups" could act like folders)
User friendliness:
    - (for the future) Case with stylus storage if keyboard is added
    - Big buttons so misclicking is less easy
    - If keyboard, have a maths keyboard/shortcuts for writing in maths mode
    - "Help" page containing how to make a flashcard etc
Design:
    - Cards are lined like a physical flashcard (and text matches up)
    - Light/dark mode options?
'''

# This stuff is just for getting a general idea of how things should work

import math
import random
import time
# Getting a random flashcard from today list
todayfc = [["What does the fox say?", "AAAA"], ["What is the meaning of life, the universe and everything?", "42"], ["Knock knock", "Who's there?"], ["Something clever", "Goes here"]]
def getacard():
    length = len(todayfc)
    cardno = random.randint(0,length)
    card = todayfc.pop(cardno)
    print(card)

'''
Idk how to do the touch input so imma just words lol

tomorrowfc = [["Some flashcards", "but for the future wow"], ["This is the second flashcard", "and I'm already running out of ideas"]]
nextweekfc = [["gruiasdjs", "jiufdsjof"], ["fjeisj", "fhiusjojw"]]
    we need a way to have a "due date" for these, but for now imma just make the sorting method

wrongbutton = user touches "wrong" button
hardbutton = user touches "hard" button
easybutton = user touches "easy" button

def setdifficulty():
    if user touches wrongbutton:
        todayfc.append(card)
    if user touches hardbutton:
        tomorrowfc.append(card)
    if user touches easybutton:
        nextweekfc.append(card)
'''

# The actual "showing" of the flashcard
'''
print(card[0])
if user touches screen:
    print(card[1])
    show wrongbutton
    show hardbutton
    show easybutton
'''