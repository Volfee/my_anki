import tkinter as tk
from page import Page
from PIL import ImageTk, Image

class MainPage(Page):

	input_underscore_color = '#939692'
	deck_font = ("SFNS", 18)

	def __init__(self, *args, **kwargs):
		self.page_name = 'My AnkiDroid'
		self.master = kwargs['master']
		Page.__init__(self, *args, **kwargs)

	# @overriden
	def left_header_icon(self, master):
		photo = ImageTk.PhotoImage(Image.open('icons/flashcards.png'))
		left_header_icon = tk.Button(master, image=photo)
		left_header_icon.image = photo
		left_header_icon['highlightbackground'] = self.header_color
		left_header_icon['highlightthickness'] = 0
		left_header_icon['command'] = self.master.show_view_all_page
		return left_header_icon

	# @overriden
	def right_header_icon(self, master):
		photo = ImageTk.PhotoImage(Image.open('icons/plus.png'))
		right_header_icon = tk.Button(master, image=photo)
		right_header_icon.image = photo
		right_header_icon['highlightbackground'] = self.header_color
		right_header_icon['highlightthickness'] = 0
		right_header_icon['command'] = self.master.show_add_flashcard_page
		return right_header_icon

	# @overriden
	def body_container(self, master):
		body = tk.Frame(master)
		body['background'] = self.background_color
		self.list_of_decks_frame(body).pack(side='top', fill='both')
		return body

	def list_of_decks_frame(self, master):
		self._list_of_decks = tk.Frame(master)
		self._list_of_decks['background'] = self.background_color
		decks = self.interface.get_deck_names()
		self.deck_divider_frame(self._list_of_decks).pack(side='top', fill='x')
		for deck_name in decks:
			self.deck_frame(self._list_of_decks, deck_name).pack(side='top', fill='x')
			self.deck_divider_frame(self._list_of_decks).pack(side='top', fill='x')
		self.add_deck_frame(self._list_of_decks).pack(side='top', fill='x')
		return self._list_of_decks

	def deck_frame(self, master, name):
		deck = tk.Frame(master)
		deck['background'] = self.background_color
		deck['height'] = 40
		deck.pack_propagate(False)
		self.deck_contents(deck, name)
		return deck

	def deck_contents(self, master, name):
		self.deck_name(master, name).pack(side='left', padx=15)
		self.deck_review_button(master, name).pack(side='right', padx=15)
		self.deck_review_count_label(master, name).pack(side='right')

	def deck_name(self, master, name):
		deck_name = tk.Label(master)
		deck_name['text'] = name
		deck_name.config(font=self.deck_font)
		deck_name['background'] = self.background_color
		return deck_name

	def deck_review_button(self, master, name):
		deck_review_button = tk.Button(master)
		deck_review_button['text'] = 'Review'
		deck_review_button['highlightbackground'] = self.background_color
		deck_review_button['command'] = lambda: self.start_deck_review_action(name)
		return deck_review_button

	def start_deck_review_action(self, deck_name):
		review = self.interface.create_review(deck_name)
		self.master.show_new_review_page(review)

	def deck_review_count_label(self, master, name):
		deck_review_count = tk.Label(master)
		deck_count = self.interface.num_cards_for_review(deck=name)
		deck_review_count['text'] = f"Cards: {deck_count}"
		deck_review_count['padx'] = 15
		deck_review_count['background'] = self.background_color
		return deck_review_count

	def deck_divider_frame(self, master):
		deck_divider = tk.Frame(master)
		deck_divider['height'] = 1
		deck_divider['background'] = self.divider_color
		deck_divider.pack_propagate(False)
		return deck_divider

	def add_deck_frame(self, master):
		self._add_deck_frame = tk.Frame(master)
		self._add_deck_frame['pady'] = 10
		self._add_deck_frame['height'] = 40
		self._add_deck_frame['bg'] = self.background_color
		self._add_deck_frame.pack_propagate(False)
		self.add_deck_button(self._add_deck_frame).pack(side='top')
		return self._add_deck_frame

	def add_deck_button(self, master):
		_add_deck_button = tk.Button(master)
		_add_deck_button['text'] = "Create new deck"
		_add_deck_button['highlightbackground'] = self.background_color
		_add_deck_button['command'] = self.new_deck_creator
		return _add_deck_button

	def new_deck_creator(self):
		self._add_deck_frame.destroy()
		self.new_deck_frame(self._list_of_decks).pack(side='top', fill='x')
		self.deck_divider_frame(self._list_of_decks).pack(side='top', fill='x')

	def new_deck_frame(self, master):
		""" Appears after add deck button ic clicked.
			Contains entry field and add button."""
		self._new_deck_frame = tk.Frame(master)
		self._new_deck_frame['height'] = 40
		self._new_deck_frame['bg'] = self.background_color
		self._new_deck_frame.pack_propagate(False)
		self.new_deck_entry_frame(self._new_deck_frame).pack(side='left', padx=20)
		self.new_deck_add_button(self._new_deck_frame).pack(side='left', padx=5)
		return self._new_deck_frame

	def new_deck_entry_frame(self, master):
		"""Frame containing entry field and underscore for entry field."""
		_new_deck_entry_frame = tk.Frame(master)
		self.new_deck_entry(_new_deck_entry_frame).pack()
		self.new_deck_entry_underscore(_new_deck_entry_frame).pack(side='top', fill='x')
		return _new_deck_entry_frame

	def new_deck_entry(self, master):
		"""Entry field to set new name of deck."""
		_new_deck_entry = tk.Entry(master)
		_new_deck_entry.config(font=self.deck_font)
		_new_deck_entry['background'] = self.background_color
		_new_deck_entry['borderwidth'] = 0
		_new_deck_entry['highlightthickness'] = 0
		return _new_deck_entry

	def new_deck_add_button(self, master):
		"""Button to approve adding new deck."""
		_new_deck_add_button = tk.Button(master)
		_new_deck_add_button['text'] = "Add"
		_new_deck_add_button['highlightbackground'] = self.background_color
		_new_deck_add_button['command'] = self.create_new_deck
		return _new_deck_add_button

	def create_new_deck(self):
		pass

	def new_deck_entry_underscore(self, master):
		"""Frame that serves as underscore for entry field."""
		underscore = tk.Frame(master)
		underscore['height'] = 1
		underscore['background'] = self.input_underscore_color
		underscore.pack_propagate(False)
		return underscore






