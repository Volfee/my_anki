class StorageManager:
	"""Handles saving and loading flashcards from drive."""
	storage = "storage/cards.json"

	def __init__(self):
		pass

	def save_card(self, flashcard):
		json_card = flashcard.to_json()
		with open(StorageManager.storage, 'a') as f:
			f.write(json_card)

	def load_card(self, id='next'):
		pass

	def load_all_cards(self):
		pass