import sqlite3
import os
from flashcards import Flashcard

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
			CREATE TABLE flashcards 
			(front text, back text, deck text, review_due int)
			""")
		conn.commit()
		conn.close()

	def db_exists(self):
		return os.path.isfile(self.db_location)

	def load_all_cards(self):
		conn = sqlite3.connect(self.db_location)
		cursor = conn.execute("""
			SELECT front, back, deck, review_due FROM flashcards
			""")
		for card in cursor:
			front, back, deck, review_due = card
			yield Flashcard(front, back, deck, review_due)
		conn.close()

	def get_pending_cards(self, deck, time):
		conn = sqlite3.connect(self.db_location)
		cursor = conn.execute("""
			SELECT front, back, deck, review_due 
			FROM flashcards
			WHERE review_due <= (?)
			""", (time,))
		for card in cursor:
			front, back, deck, review_due = card
			yield Flashcard(front, back, deck, review_due)
		conn.close()

	def clear_storage(self):
		pass

	def remove_card(self, flashcard):
		conn = sqlite3.connect(self.db_location)
		cursor = conn.execute("""
			DELETE FROM flashcards
			WHERE front = (?)
			""", (flashcard.front,))
		conn.commit()
		conn.close()
