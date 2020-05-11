from flashcards import Flashcard
from storage_manager import StorageManager

class UserInterface:

	def create_new_card(self, front, back):
		flashcard = Flashcard(front, back)
		sm = StorageManager() 
		sm.save_card(flashcard)
		print("New {0} created.".format(flashcard))

	def load_all_cards(self):
		sm = StorageManager()
		cards = sm.load_all_cards()

		return cards

	def remove_card(self, flashcard):
		sm = StorageManager()
		cards = sm.remove_card(flashcard)


ui = UserInterface()
