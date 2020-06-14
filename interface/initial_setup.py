import os
import datetime as dt
from backend.storage_manager import StorageManager
from backend.interface import UserInterface

class InitialSetup():
	sm = StorageManager()
	ui = UserInterface()

	def setup(cards=None, decks=None):
		InitialSetup.rebuild_db()
		InitialSetup.add_decks()
		InitialSetup.add_flashcards()


	def rebuild_db():
		if os.path.isfile('./backend/storage/flashcards.db'):
			os.remove('./backend/storage/flashcards.db')
		InitialSetup.sm._create_database()


	def add_decks():
		test_decks = ['english', 'german', 'spanish']
		for deck in test_decks:
			InitialSetup.sm.add_deck(deck)

	def date_offset(d):
		return InitialSetup.ui.current_date + dt.timedelta(days=d)

	def add_flashcards():
		InitialSetup.ui.create_new_card('toy', 'zabawka')
		InitialSetup.ui.create_new_card('car', 'samochod')
		InitialSetup.ui.create_new_card('picture', 'obraz')
		InitialSetup.ui.create_new_card('cup', 'kubek')
		InitialSetup.ui.create_new_card('post', 'poczta', due=InitialSetup.date_offset(2))
		InitialSetup.ui.create_new_card('fridge', 'lodowka', due=InitialSetup.date_offset(3))
		InitialSetup.ui.create_new_card('newspaper', 'gazeta', due=InitialSetup.date_offset(-2))
		InitialSetup.ui.create_new_card('lightbulb', 'zarowka', due=InitialSetup.date_offset(-3))
		InitialSetup.ui.create_new_card('kon', 'el poyo', 'spanish')
		InitialSetup.ui.create_new_card('money', 'las platas', 'spanish')
		InitialSetup.ui.create_new_card('coke', 'el coke', 'spanish', due=InitialSetup.date_offset(1))
		InitialSetup.ui.create_new_card('paella', 'paella', 'spanish', due=InitialSetup.date_offset(2))
		InitialSetup.ui.create_new_card('plate', 'das pommel', 'german')
		InitialSetup.ui.create_new_card('good day', 'guten morgen', 'german')
		InitialSetup.ui.create_new_card('hands up', 'hende hoh', 'german', due=InitialSetup.date_offset(1))

if __name__ == '__main__':
	InitialSetup.setup()