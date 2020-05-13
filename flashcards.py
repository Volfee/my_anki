import sqlite3

class Flashcard:

	db = 'storage/flashcards.db'

	def __init__(self, front, back, deck='default', review_due=None):
		self.front = front
		self.back = back
		self.deck = deck
		self.review_due = review_due

	def __repr__(self):
		return f"Flashcard('{self.front}', '{self.back}')"

	def save_to_db(self):
		conn = sqlite3.connect(self.db)
		conn.execute("""
			INSERT INTO flashcards
			VALUES (?, ?, ?, ?)
			""", self.to_tuple())
		conn.commit()
		conn.close()

	def update_due_date(self, new_due_date):
		self.review_due = new_due_date
		conn = sqlite3.connect(self.db)
		conn.execute("""
			UPDATE flashcards
			SET review_due = (?)
			WHERE front = (?) 
			""", (self.review_due, self.front))
		conn.commit()
		conn.close()

	def to_tuple(self):
		return self.front, self.back, self.deck, self.review_due


class Base(Flashcard):
	pass


class Cloze(Flashcard):
	pass