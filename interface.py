from flashcards import Flashcard
from storage_manager import StorageManager

class UserInterface:

	current_deck = {}

	def create_new_card(self, front, back):
		flashcard = Flashcard(front, back)
		flashcard.save()
		self.current_deck['flashcard.id'] = flashcard
		print("New {0} created.".format(flashcard))

	def load_all_cards(self):
		sm = StorageManager()
		cards = list(sm.load_all_cards())
		self.current_deck = {card.id:card for card in cards}


ui = UserInterface()
ui.create_new_card('auto', 'car')
ui.create_new_card('klawiatura', 'keyboard')
ui.create_new_card('lampka', 'light')


# ui.load_all_cards()
# for card in ui.current_deck.values():
#  	print(card)

