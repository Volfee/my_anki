import sys
import datetime as dt
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
		self.current_card.correct_streak += 1
		next_review_delta = 2 ** self.current_card.correct_streak
		next_review_date = dt.date.today() + dt.timedelta(days=next_review_delta)
		self.current_card.review_due = next_review_date
		print(f'Card due changed to {next_review_date}')
		self.current_card = None

	def wrong_answer(self):
		self.current_card.correct_streak = 0
		self.cards.append(self.current_card)
		self.current_card = None

	def is_finished(self):
		return not len(self.cards)

	@property
	def cards_left(self):
		return len(self.cards)
