"""
Main menu page
^^^^^^^^^^^^^^
* List of decks
	* Shows number of cards in each deck
	* Option to start reviews -> Page: reviews
* Create new card -> Page: create new card
* View all cards
* Stats -> Page: show stats

"""
import tkinter as tk

class Application(tk.Frame):

	background_color = '#f7fff7'
	head_frame_color = '#4ecdc4'
	deck_color = "#f7fff7"
	header_font = "SFNS", 30

	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.master.title("My AnkiDroid Clone")
		self.master.geometry('400x800')
		self.master['bg'] = self.background_color
		self.pack()
		self.head_frame()
		self.list_of_decks_frame()
		self.add_flashcard_frame()

	def head_frame(self):
		self.head_frame = tk.Frame(self.master)
		self.head_frame['height'] = 50
		self.head_frame['width'] = 400
		self.head_frame['background'] = self.head_frame_color
		self.head_frame.pack_propagate(False)
		self.head_frame.pack(side='top')
		self.head_label()

	def head_label(self):
		self.head = tk.Label(self.head_frame)
		self.head['text'] = "My AnkiDroid Clone"
		self.head['background'] = self.head_frame_color
		self.head.config(font=self.header_font)
		self.head.pack(side='bottom')

	def list_of_decks_frame(self):
		self.list_of_decks = tk.Frame(self.master)
		self.list_of_decks['height'] = 580
		self.list_of_decks['width'] = 400
		self.list_of_decks['background'] = self.background_color
		self.list_of_decks.pack_propagate(False)
		self.list_of_decks.pack(side='top')
		decks = ['Default', 'Python', 'Java']
		for deck_name in decks:
			self.deck_frame(deck_name)
			self.deck_divider_frame()

	def deck_frame(self, name):
		self.deck = tk.Frame(self.list_of_decks)
		self.deck['height'] = 50
		self.deck['width'] = 400
		self.deck['background'] = self.deck_color
		self.deck.pack_propagate(False)
		self.deck.pack(side='top')
		self.deck_contents(name)

	def deck_contents(self, name):
		self.deck_name_label(name)
		self.deck_review_button(name)
		self.deck_review_count_label(name)

	def deck_name_label(self, name):
		self.deck_name = tk.Label(self.deck)
		self.deck_name['text'] = name
		self.deck_name.config(font=("SFNS", 18))
		self.deck_name['background'] = self.deck_color
		self.deck_name.pack(side='left', padx=15)

	def deck_review_count_label(self, name):
		self.deck_review_count = tk.Label(self.deck)
		self.deck_review_count['text'] = "Cards: 10"
		self.deck_review_count['padx'] = 15
		self.deck_review_count['background'] = self.deck_color
		self.deck_review_count.pack(side='right')

	def deck_review_button(self, name):
		self.deck_review = tk.Button(self.deck)
		self.deck_review['text'] = 'Review'
		self.deck_review['highlightbackground'] = self.deck_color
		self.deck_review.pack(side='right', padx=15)

	def deck_divider_frame(self):
		self.deck_divider = tk.Frame(self.list_of_decks)
		self.deck_divider['height'] = 1
		self.deck_divider['width'] = 400
		self.deck_divider['background'] = "#eef0e9"
		self.deck_divider.pack_propagate(False)
		self.deck_divider.pack(side='top')

	def add_flashcard_frame(self):
		self.add_flashcard = tk.Frame(self.master)
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
		self.add_flashcard_button['height'] = 60
		self.add_flashcard_button['width'] = 400
		self.add_flashcard_button['highlightbackground'] = self.head_frame_color
		self.add_flashcard_button.pack(side='bottom')

root = tk.Tk()
app = Application(master=root)
app.mainloop()
