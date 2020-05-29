from backend.flashcards import Flashcard
from backend.storage_manager import StorageManager
from backend.review import Review

class UserInterface:

	current_time = 10 # temp 
	sm = StorageManager()

	def create_new_card(self, front, back, deck='default', due=None):
		if not due:
			due = self.current_time
		if self.is_new_deck(deck):
			self.add_deck(deck)
		flashcard = Flashcard(front, back, deck, review_due=due)
		flashcard.save_to_db()
		print(f"New {flashcard} created.")

	def is_new_deck(self, deck_name):
		return deck_name not in self.get_deck_names()

	def add_deck(self, deck_name):
		self.sm.add_deck(deck_name)

	def load_all_cards(self):
		cards = self.sm.load_all_cards()
		return cards

	def show_all_cards(self):
		for card in self.load_all_cards():
			print(card)

	def remove_card(self, flashcard):
		sm = StorageManager()
		cards = self.sm.remove_card(flashcard)

	def create_review(self, deck=None):
		pending_cards = self.sm.get_pending_cards(deck, self.current_time)
		return Review(pending_cards)

	def get_deck_names(self):
		deck_names = self.sm.get_deck_names()
		return list(deck_names)

	def num_cards_for_review(self, deck):
		count = self.sm.num_cards_for_review(deck, self.current_time)
		return count





# ui = UserInterface()
# k = ui.get_deck_names()

# if __name__ == "__main__":
# 	ui = UserInterface()
# 	k = ui.get_deck_names()
# 	print(k)
	#ui.show_all_cards()


	# Create some flashcards.
	# ui.create_new_card('toy', 'zabawka')
	# ui.create_new_card('car', 'samochod')
	# ui.create_new_card('picture', 'obraz')
	# ui.create_new_card('cup', 'kubek')
	# ui.create_new_card('post', 'poczta', 2)
	# ui.create_new_card('fridge', 'lodowka', 3)

	# ui.create_new_card('toy', 'el toy', 'spanish', 0)
	# ui.create_new_card('car', 'el car', 'spanish', 0)
	# ui.create_new_card('picture', 'el picture', 'spanish', 1)
	# ui.create_new_card('post', 'el post', 'spanish', 2)

	# ui.create_new_card('toy', 'das toy', 'german', 0)
	# ui.create_new_card('car', 'das car', 'german', 0)
	# ui.create_new_card('picture', 'das picture', 'german', 1)
	# ui.create_new_card('post', 'das post', 'german', 2)

	 

	# Create review
	# review = ui.create_review()
	# ui.start_review(review)

	# ui.show_all_cards()

	# Start reviewing

	# review = ui.start_review()

