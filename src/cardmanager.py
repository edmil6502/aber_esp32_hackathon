'''

	cardmanager.py

	Backend code. Stores cards, gives a random card through 'getCard()'.
	Called by 'showcard'

'''

import random

# flashcards = [["where is pee stored", "**REDACTED**"], ["what is the best animal?", "horse"], ["who is the Super Hero?", "hong kong phooey (no.1 super guy!)"]]

flashcards = {0 : ["where is pee stored", "the balls"], 1 : ["what is the best animal?", "horse"], 2 : ["who is the Super Hero?", "hong kong phooey (no.1 super guy!)"]}

def getCard():
	x = random.choice(flashcards)
	return x
