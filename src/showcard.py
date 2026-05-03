'''

	showcard.py

	Shows a card to the user. The user should see the question first, then tap the screen to reveal the answer. 

'''

import init
import lvgl as lv

import cardmanager

import random
import time

scr = lv.screen_active()


questionText = lv.label(scr)
answerText = lv.label(scr)

questionText.set_pos(60, 50)
answerText.set_pos(60, 100)


button = lv.button(scr)
button.center()

# update what is on screen to match the contents of the card
while True:
	card = cardmanager.getCard()

	questionText.set_text(card[0])
	answerText.set_text(card[1])
	time.sleep(5)

def removeCard():
	print("greer")
	
button.add_event_cv(removeCard, lvgl.EVENT.ALL, None)
