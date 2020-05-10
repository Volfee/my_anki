import json

class StorageManager:
	"""Handles saving and loading flashcards from drive."""
	storage = 'storage/cards.json'
	metadata = 'storage/metadata'

	def __init__(self, storage=None):
		if storage:
			self.storage = storage

	def save_card(self, flashcard):
		with open(self.storage, 'a') as file:
			json.dump(flashcard.to_dict(), file)
		self.store_last_id(flashcard.id)

	def load_all_cards(n=0):
		with open(self.storage) as cards_file:
			cards = json.load(cards_file)
		return cards

	def get_last_id(self):
		try:
			with open(self.metadata) as meta:
				metadict = json.load(meta)
			return metadict['last_id']

		except json.decoder.JSONDecodeError as err:
			print("No cards in database yet. Returning id 1.")
			return 0

	def store_last_id(self, last_id):
		to_save = {'last_id': last_id}
		with open(self.metadata, 'w') as meta:
			json.dump(to_save, meta)

	def clear_storage(self):
		pass

	def remove_card(self):
		"""Removing card will result in ids mismatching number of rows.
		Changes to get_last_id will have to be made.
		"""
		pass
