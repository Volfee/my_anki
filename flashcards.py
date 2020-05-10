from storage_manager import StorageManager

class Flashcard:
	last_id = 0
	sm = StorageManager()

	def __init__(self, front, back, deck='default', id=None):
		if id:
			self.id = id
		else:
			self.id = self._create_id()
		self.front = front
		self.back = back

	def _create_id(self):
		if not Flashcard.last_id:
			Flashcard.last_id = self.sm.get_last_id()
		Flashcard.last_id += 1
		return Flashcard.last_id

	def save(self):
		self.sm.save_card(self)

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