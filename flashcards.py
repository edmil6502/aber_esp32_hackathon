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


# Inputting flashcards on the esp32:
todayfc = []
words = input() # Input both sides seperated by ::
todayfc.append(fc) # Add new flashcard to list of flashcards to do today
#print(todayfc)

