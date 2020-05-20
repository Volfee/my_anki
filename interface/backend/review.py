import sys
sys.path.append('../')

import collections

class Review:

	def __init__(self, cards):
		self.cards = collections.deque(cards)
		self.current_card = None

	def next_card(self):
		self.current_card = self.cards.popleft()
		return self.current_card

	def correct_answer(self):
		new_due_date = (self.current_card.review_due + 1) * 2
		self.current_card.review_due = new_due_date
		print(f'Card due changed to {new_due_date}')
		self.current_card = None

	def wrong_answer(self):
		self.cards.append(self.current_card)
		self.current_card = None

	def is_finished(self):
		return not len(self.cards)

	@property
	def cards_left(self):
		return len(self.cards)
