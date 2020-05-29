import os
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

	def add_flashcards():
		InitialSetup.ui.create_new_card('toy', 'zabawka')
		InitialSetup.ui.create_new_card('car', 'samochod')
		InitialSetup.ui.create_new_card('picture', 'obraz')
		InitialSetup.ui.create_new_card('cup', 'kubek')
		InitialSetup.ui.create_new_card('post', 'poczta', due=2)
		InitialSetup.ui.create_new_card('fridge', 'lodowka', due=3)
		InitialSetup.ui.create_new_card('toy', 'el toy', 'spanish', 0)
		InitialSetup.ui.create_new_card('car', 'el car', 'spanish', 0)
		InitialSetup.ui.create_new_card('picture', 'el picture', 'spanish', 1)
		InitialSetup.ui.create_new_card('post', 'el post', 'spanish', 2)
		InitialSetup.ui.create_new_card('toy', 'das toy', 'german', 0)
		InitialSetup.ui.create_new_card('car', 'das car', 'german', 0)
		InitialSetup.ui.create_new_card('picture', 'das picture', 'german', 1)

if __name__ == '__main__':
	InitialSetup.setup()