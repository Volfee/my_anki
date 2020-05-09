import json

class Flashcard:
	next_id = 0

	def __init__(self, front, back='', deck='default', id=None):
		if id:
			self.id = id
		else:
			self.id = self._create_id()
		self.front = front
		self.back = back

	def to_json(self):
		"""Returns json representation of the card."""
		flashcard = {
			'id': self.id,
			'front': self.front,
			'back': self.back
		}
		json_card = json.dumps(flashcard)
		return json_card

	def _check_next_id(self):
		Flashcard.next_id = StorageManager.get_last_id() + 1

	def _create_id(self):
		if Flashcard.next_id == 0:
			self._check_next_id()
		return Flashcard.next_id



class Base(Flashcard):
	pass

class Cloze(Flashcard):
	pass