class Flashcard:
	def __init__(self, front, back, deck='default'):
		self.front = front
		self.back = back
		self.deck = deck

	def __repr__(self):
		return f"Flashcard('{self.front}', '{self.back}')"

class Base(Flashcard):
	pass


class Cloze(Flashcard):
	pass