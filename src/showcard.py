'''

	showcard.py

	

'''

import init
import lvgl as lv

scr = lv.screen_active()

flashcards = [["where is pee stored", "the balls"], ["what is the best animal?", "horse"]]
card = flashcards[0]

questionText = lv.label(scr)
questionText.set_text(card[0])
questionText.set_pos(60, 50)

answerText = lv.label(scr)
answerText.set_text(card[1])
answerText.set_pos(60, 100)
