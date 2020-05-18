import tkinter as tk
from PIL import ImageTk, Image
from page import Page
from backend.interface import UserInterface
import collections
from backend.flashcards import Flashcard

class ReviewPage(Page):

	input_label_font = 'Verdana', 15
	input_font = 'Verdana', 25


	def __init__(self, *args, **kwargs):
		self.master = kwargs['master']
		ReviewPage.cards = collections.deque([Flashcard('samochod', 'car', 'default', 2),
											  Flashcard('narty', 'ski', 'default', 1)])

		deck_name = 'default'
		cards_left = 5

		self.page_name = f"{deck_name} | Cards left: {cards_left}."
		self.answer_displayed = False
		self.card = ReviewPage.cards.popleft()
		Page.__init__(self, *args, **kwargs)
		

	# @overriden
	def body_container(self, master):
		self.body = tk.Frame(master)
		self.body['background'] = self.background_color
		self.flashcard_frame(self.body, "Front", self.card.front) \
							.pack(side='top', fill='both')
		return self.body

	def flashcard_frame(self, master, label, value):
		front_frame = tk.Frame(master)
		self.front_frame_label(front_frame, label).pack(side="top", fill="x")
		self.front_frame_value(front_frame, value).pack(side="top", fill="x")
		return front_frame

	def front_frame_label(self, master, label):
		front_frame_label = tk.Label(master)
		front_frame_label['text'] = f'{label}:'
		front_frame_label['font'] = self.input_label_font
		front_frame_label['anchor'] = 'sw'
		front_frame_label['bg'] = self.background_color
		front_frame_label['padx'] = 20
		front_frame_label['pady'] = 15
		return front_frame_label

	def front_frame_value(self, master, value):
		front_frame_value = tk.Label(master)
		front_frame_value['text'] = f"{value}"
		front_frame_value['bg'] = self.background_color
		front_frame_value['font'] = self.input_font
		front_frame_value['justify'] = 'center'
		return front_frame_value

	# @overridden
	def footer(self, master):
		self.footer_frame = tk.Frame(master)
		self.show_answer_button(self.footer_frame).pack(side='bottom', fill='x')
		return self.footer_frame

	def show_answer_button(self, master):
		self.answer_button = tk.Button(master)
		self.answer_button['text'] = "Show answer"
		self.answer_button['height'] = 5
		self.answer_button['highlightbackground'] = self.header_color
		self.answer_button['command'] = self.show_answer
		return self.answer_button

	def show_answer(self):
		if not self.answer_displayed:
			self.flashcard_frame(self.body, "Back", self.card.back) \
								.pack(side='top', fill='x')
			self.answer_displayed = True
			self.answer_button.destroy()
			self.wrong_answer_button(self.footer_frame) \
							.pack(side='left', fill='both', expand=True)
			self.good_answer_button(self.footer_frame)\
							.pack(side='right', fill='both', expand=True)
			# Change buttons to good / bad

	def wrong_answer_button(self, master):
		wrong_answer = tk.Button(master)
		wrong_answer['text'] = 'Wrong'
		wrong_answer['highlightbackground'] = 'red'
		wrong_answer['height'] = 5
		return wrong_answer

	def good_answer_button(self, master):
		good_answer = tk.Button(master)
		due_change = 2
		good_answer['text'] = f'Good ({due_change}d)'
		good_answer['highlightbackground'] = 'green'
		good_answer['height'] = 5
		good_answer['command'] = self.good_answer
		return good_answer

	def good_answer(self):
		self.master.review_page = ReviewPage(master=self.master)
		self.master.review_page.show()


if __name__ == '__main__':
	app = tk.Tk()
	app.title("My AnkiDroid Clone")
	main = ReviewPage(app)
	main.pack(side="top", fill="both", expand=True)
	app.geometry('400x800')
	app.mainloop()