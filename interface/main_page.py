import tkinter as tk
from page import Page
from PIL import ImageTk, Image

def overrides(interface_class):
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider

class MainPage(Page):

	def __init__(self, *args, **kwargs):
		self.page_name = 'My AnkiDroid'
		self.master = kwargs['master']
		Page.__init__(self, *args, **kwargs)
	
	# @overridden
	def body_container(self, master):
		body = tk.Frame(master)
		body['background'] = self.background_color
		self.list_of_decks_frame(body).pack(side='top', fill='both')
		return body

	def list_of_decks_frame(self, master):
		list_of_decks = tk.Frame(master)
		list_of_decks['background'] = self.background_color
		decks = ['Default', 'Python', 'Java']
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
		return deck_review_button


	def deck_review_count_label(self, master, name):
		deck_review_count = tk.Label(master)
		deck_review_count['text'] = "Cards: 10"
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


"""
	def add_flashcard_frame(self):
		self.add_flashcard = tk.Frame(self)
		self.add_flashcard['background'] = self.head_frame_color
		self.add_flashcard['height'] = 60
		self.add_flashcard['width'] = 400
		self.add_flashcard['bg'] = self.head_frame_color
		self.add_flashcard.pack_propagate(False)
		self.add_flashcard.pack(side='bottom')
		self.create_flashcard_button()

	def create_flashcard_button(self):
		self.add_flashcard_button = tk.Button(self.add_flashcard)
		self.add_flashcard_button['text'] = "Add new flashcard"
		self.add_flashcard_button['command'] = self.master.add_flashcard_page.show
		self.add_flashcard_button['height'] = 60
		self.add_flashcard_button['width'] = 400
		self.add_flashcard_button['highlightbackground'] = self.head_frame_color
		self.add_flashcard_button.pack(side='bottom')
"""