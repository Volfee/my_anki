class Flashcard:
	def __init__(self, front, back, deck='default', review_due=None):
		self.front = front
		self.back = back
		self.deck = deck
		self.review_due = review_due

	def __repr__(self):
		return f"Flashcard('{self.front}', '{self.back}')"

class Base(Flashcard):
	pass


class Cloze(Flashcard):
	pass