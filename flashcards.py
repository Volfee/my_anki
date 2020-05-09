class Flashcard:
	next_id = 0

	def __init__(self, front, back='', deck='default'):
		self.id = self.create_id()
		self.front = front
		self.back = back

	def save(self):
		"""Saves flashcard to file."""
		pass

	def _create_id(self):
		Flashcard.next_id += 1
		return next_id

class Base(Flashcard):
	pass

class Cloze(Flashcard):
	pass