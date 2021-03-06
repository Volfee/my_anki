import sqlite3
import os
import datetime as dt
from backend.flashcards import Flashcard

"""
Flashcards (DB):

flashcards (Table):
	 front text
	 back text
	 deck text
	 review_due int

decks (Table):
	deck text

"""

class StorageManager:
	"""Handles saving and loading flashcards from drive."""

	db_location = 'backend/storage/flashcards.db'

	def __init__(self, db=None):
		if db:
			self.db_location = db
		if not self.db_exists():
			# TODO: Db may exist but table may not.
			self._create_db()

	def _create_database(self):
		"""If DB is not found create new database."""
		conn = sqlite3.connect(self.db_location)
		conn.execute("""
			CREATE TABLE flashcards 
			(front text, back text, deck text, review_due int, correct_streak int)
			""")
		conn.commit()
		conn.execute("""
			CREATE TABLE decks 
			(deck text)
			""")
		conn.commit()
		conn.close()

	def db_exists(self):
		return os.path.isfile(self.db_location)

	def load_all_cards(self):
		all_cards = list()
		conn = sqlite3.connect(self.db_location)
		cursor = conn.execute("""
			SELECT front, back, deck, review_due, correct_streak FROM flashcards
			""")
		for card in cursor:
			front, back, deck, review_due_ordinal, correct_streak = card
			review_due = dt.date.fromordinal(review_due_ordinal)
			all_cards.append(Flashcard(front, back, deck, review_due, correct_streak))
		conn.close()
		return all_cards

	def get_pending_cards(self, deck, time):
		pending_cards = list()
		conn = sqlite3.connect(self.db_location)
		cursor = conn.execute("""
			SELECT front, back, deck, review_due, correct_streak
			FROM flashcards
			WHERE review_due <= (?)
			AND deck = (?)
			""", (time,deck))
		for card in cursor:
			front, back, deck, review_due_ordinal, correct_streak = card
			review_due = dt.date.fromordinal(review_due_ordinal)
			pending_cards.append(Flashcard(front, back, deck, review_due, correct_streak))
		conn.close()
		return pending_cards

	def num_cards_for_review(self, deck_name, time):
		conn = sqlite3.connect(self.db_location)
		cursor = conn.execute("""
			SELECT count(1)
			FROM flashcards
			WHERE deck = (?)
			AND review_due <= (?)
			""", (deck_name, time))
		count = next(cursor)
		conn.close()
		return count[0]

	def add_deck(self, deck_name):
		conn = sqlite3.connect(self.db_location)
		cursor = conn.execute("""
			INSERT INTO decks
			VALUES (?)
			""", (deck_name,))
		conn.commit()
		conn.close()

	def get_deck_names(self):
		conn = sqlite3.connect(self.db_location)
		cursor = conn.execute("""
			SELECT deck
			FROM decks
			""")
		for deck in cursor:
			yield deck[0]
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
