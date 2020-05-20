import tkinter as tk
from page import Page
from PIL import ImageTk, Image

class MainPage(Page):

	def __init__(self, *args, **kwargs):
		self.page_name = 'My AnkiDroid'
		self.master = kwargs['master']
		# self.update()
		Page.__init__(self, *args, **kwargs)

	# # @overriden
	# def show(self):
	# 	self.update()
	# 	self.lift()
	
	# def update(self):
	# 	# get list of decks
	# 	# get list of flashcards
	# 	pass

	# @overriden
	def body_container(self, master):
		body = tk.Frame(master)
		body['background'] = self.background_color
		self.list_of_decks_frame(body).pack(side='top', fill='both')
		return body

	def list_of_decks_frame(self, master):
		list_of_decks = tk.Frame(master)
		list_of_decks['background'] = self.background_color
		decks = self.interface.get_deck_names()
		self.deck_divider_frame(list_of_decks).pack(side='top', fill='x')
		for deck_name in decks:
			self.deck_frame(list_of_decks, deck_name).pack(side='top', fill='x')
			self.deck_divider_frame(list_of_decks).pack(side='top', fill='x')
		return list_of_decks

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
		deck_name.config(font=("SFNS", 18))
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
		self.master.create_new_review_page(review)
		self.master.review_page.show()

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

	# @overriden
	def left_header_icon(self, master):
		photo = ImageTk.PhotoImage(Image.open('icons/flashcards.png'))
		left_header_icon = tk.Label(master, image=photo)
		left_header_icon.image = photo
		left_header_icon['bg'] = self.header_color
		return left_header_icon

	# @overriden
	def right_header_icon(self, master):
		photo = ImageTk.PhotoImage(Image.open('icons/plus.png'))
		right_header_icon = tk.Button(master, image=photo)
		right_header_icon.image = photo
		right_header_icon['highlightbackground'] = self.header_color
		right_header_icon['highlightthickness'] = 0
		right_header_icon['command'] = lambda: self.master.add_flashcard_page.show()
		return right_header_icon
