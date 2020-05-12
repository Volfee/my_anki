import collections

class Review:

	def __init__(self, cards):
		self.cards = collections.deque(list(cards))
		self.current_card = None

	def next_card(self):
		if self.current_card:
			print("Still pending answer.")
			return None
		self.current_card = self.cards.popleft()
		return self.current_card

	def correct_answer(self):
		current_card.review_due = (current_card.review_due + 1) * 2
		print('Card due changed to {0}'.format(current_card.review_due))
		self.current_card = None

	def wrong_answer(self):
		self.cards.append(current_card.review_due)
		self.current_card = None

	def is_finished(self):
		return not len(self.cards)
