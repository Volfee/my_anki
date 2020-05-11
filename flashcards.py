from storage_manager import StorageManager

class Flashcard:
	sm = StorageManager()

	def __init__(self, front, back, deck='default'):
		self.front = front
		self.back = back
		self.deck = deck

	def __repr__(self):
		return f"Flashcard('{self.front}', '{self.back}')"

	def to_dict(self):
		"""Returns json representation of the card."""
		dictionary = {
			'id': self.id,
			'front': self.front,
			'back': self.back
		}
		return dictionary


class Base(Flashcard):
	pass


class Cloze(Flashcard):
	pass