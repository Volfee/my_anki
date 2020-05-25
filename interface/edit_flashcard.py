import tkinter as tk
from page import Page
from add_flashcard import AddFlashcard
from PIL import ImageTk, Image

class EditCardPage(AddFlashcard):

	def __init__(self, flashcard, *args, **kwargs):
		self.page_name = 'Edit flashcard'
		self.flashcard = flashcard
		Page.__init__(self, *args, **kwargs)

	# @overriden
	def left_header_icon(self, master):
		photo = ImageTk.PhotoImage(Image.open('icons/back_arrow.png'))
		left_header_icon = tk.Button(master, image=photo)
		left_header_icon.image = photo
		left_header_icon['highlightbackground'] = self.header_color
		left_header_icon['highlightthickness'] = 0
		# left_header_icon['command'] = self.master.show_view_all_page()
		return left_header_icon

	# @overriden
	def right_header_icon(self, master):
		photo = ImageTk.PhotoImage(Image.open('icons/plus.png'))
		right_header_icon = tk.Button(master, image=photo)
		right_header_icon.image = photo
		right_header_icon['highlightbackground'] = self.header_color
		right_header_icon['highlightthickness'] = 0
		# right_header_icon['command'] = self.add_flashcard
		return right_header_icon

	# @overriden
	def named_input_entry(self, master, name):
		_named_input = tk.Entry(master)
		_named_input['bg'] = self.background_color
		_named_input['borderwidth'] = 0
		_named_input['highlightthickness'] = 0
		_named_input['font'] = self.input_font
		_named_input['justify'] = 'center'
		value_to_input = getattr(self.flashcard, name, "Error")
		_named_input.insert(0, value_to_input)
		self.inputs[name] = _named_input
		return _named_input

if __name__ == '__main__':
	from backend.flashcards import Flashcard


	app = tk.Tk()
	app.title("My AnkiDroid Clone")
	flash = Flashcard('samochod', 'car')
	main = EditCardPage(master=app, flashcard=flash)
	main.pack(side="top", fill="both", expand=True)
	app.geometry('400x800')
	app.mainloop()