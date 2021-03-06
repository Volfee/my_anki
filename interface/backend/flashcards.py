import sqlite3
import datetime

class Flashcard:

	db = 'backend/storage/flashcards.db'

	def __init__(self, front, back, deck='default', review_due=None, correct_streak=0):
		self._front = front
		self._back = back
		self.deck = deck
		self._review_due = review_due
		self._correct_streak = correct_streak

	def __repr__(self):
		return f"Flashcard('{self._front}', '{self._back}', '{self.deck}', '{self._review_due}')"

	def save_to_db(self):
		conn = sqlite3.connect(self.db)
		conn.execute("""
			INSERT INTO flashcards
			VALUES (?, ?, ?, ?, ?)
			""", self.to_tuple())
		conn.commit()
		conn.close()

	@property
	def front(self):
		return self._front

	@front.setter
	def front(self, new_front):
		self._front = new_front
		conn = sqlite3.connect(self.db)
		conn.execute("""
			UPDATE flashcards
			SET front = (?)
			WHERE front = (?) 
			""", (self._front, self._front))
		conn.commit()
		conn.close()
		print(f'{self} edited, front updated.')

	@property
	def back(self):
		return self._back

	@back.setter
	def back(self, new_back):
		self._back = new_back
		conn = sqlite3.connect(self.db)
		conn.execute("""
			UPDATE flashcards
			SET back = (?)
			WHERE front = (?) 
			""", (self._back, self._front))
		conn.commit()
		conn.close()
		print(f'{self} edited, back updated.')

	@property
	def review_due(self):
		return self._review_due

	@review_due.setter
	def review_due(self, new_due_date: datetime.date):
		self._review_due = new_due_date
		conn = sqlite3.connect(self.db)
		conn.execute("""
			UPDATE flashcards
			SET review_due = (?)
			WHERE front = (?) 
			""", (self._review_due.toordinal(), self._front))
		conn.commit()
		conn.close()
		print(f'{self} edited, review_due updated.')

	@property
	def correct_streak(self):
		return self._correct_streak

	@correct_streak.setter
	def correct_streak(self, correct_streak):
		self._correct_streak = correct_streak
		conn = sqlite3.connect(self.db)
		conn.execute("""
			UPDATE flashcards
			SET correct_streak = (?)
			WHERE front = (?) 
			""", (self._correct_streak, self._front))
		conn.commit()
		conn.close()
		print(f'{self} edited, correct_streak updated.')

	def to_tuple(self):
		return self._front, self._back, self.deck, self._review_due.toordinal(), self._correct_streak

	def remove(self):
		conn = sqlite3.connect(self.db)
		conn.execute("""
			DELETE FROM flashcards
			WHERE front = (?) 
			""", (self._front,))
		conn.commit()
		conn.close()
		print(f"{self} removed from db.")



class Base(Flashcard):
	pass


class Cloze(Flashcard):
	pass