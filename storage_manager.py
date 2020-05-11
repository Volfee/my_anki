import sqlite3
import os

class StorageManager:
	"""Handles saving and loading flashcards from drive."""

	db_location = 'storage/flashcards.db'

	def __init__(self, db=None):
		if db:
			self.db_location = db
		if not self.db_exists():
			# TODO: Db may exist but table may not.
			self._create_db()

	def _create_db(self):
		"""If DB is not found create new database."""
		conn = sqlite3.connect(self.db_location)
		conn.execute("""
			CREATE TABLE flashcards (front text, back text, deck text)
			""")
		conn.commit()
		conn.close()

	def db_exists(self):
		return os.path.isfile(self.db_location)

	def save_card(self, flashcard):
		conn = sqlite3.connect(self.db_location)
		conn.execute("""
			INSERT INTO flashcards
			VALUES (?,?,?)""", (flashcard.front,flashcard.back, flashcard.deck)
			)
		conn.commit()
		conn.close()

	def get_last_id(self):
		pass

	def load_all_cards(self):
		pass

	def clear_storage(self):
		pass

	def remove_card(self):
		pass
