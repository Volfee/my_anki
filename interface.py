from flashcards import Flashcard
from storage_manager import StorageManager
from review import Review

class UserInterface:

	current_time = 0 # temp 
	sm = StorageManager()

	def create_new_card(self, front, back, due=None):
		if not due:
			due = self.current_time
		flashcard = Flashcard(front, back, review_due=due)
		sm = StorageManager() 
		sm.save_card(flashcard)
		print("New {0} created.".format(flashcard))

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

	def start_review(self, review):
		print("Starting review")
		while not review.is_finished():
			card = review.next_card()
			input(card.front)
			print(card.back)
			is_correct = input("Correct answer? (y/n): ")
			if is_correct == 'y':
				review.correct_answer()
			else:
				review.correct_answer()



ui = UserInterface()
#ui.show_all_cards()


# Create some flashcards.
# ui.create_new_card('plane', 'samolot')
# ui.create_new_card('car', 'samochod')
# ui.create_new_card('picture', 'obraz')
# ui.create_new_card('cup', 'kubek')
# ui.create_new_card('post', 'poczta', 2)
# ui.create_new_card('fridge', 'lodowka', 3)

# Create review
review = ui.create_review()
ui.start_review(review)



# Start reviewing

# review = ui.start_review()

