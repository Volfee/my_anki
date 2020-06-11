import tkinter as tk
from page import Page
from PIL import ImageTk, Image
from backend.interface import UserInterface
from initial_setup import InitialSetup

class AddFlashcard(Page):

	inputs = {}
	interface = UserInterface()

	input_underscore_color = '#939692'

	input_label_font = 'Verdana', 15
	input_font = 'Verdana', 25

	def __init__(self, *args, **kwargs):
		self.page_name = 'Create new card'
		Page.__init__(self, *args, **kwargs)

	def add_flashcard(self):
		front = self.inputs['front'].get()
		back = self.inputs['back'].get()
		deck = self.inputs['deck'].get()
		if front and back:
			self.interface.create_new_card(front, back, deck)
			self.reset_inputs(self.inputs['front'], self.inputs['back'])
		else:
			print("Missing front or back.")

	def reset_inputs(self, *args):
		for _input in args:
			_input.delete(0, tk.END)

	# @overriden
	def body_container(self, master):
		body = tk.Frame(master)
		body['background'] = self.background_color
		self.input_frame(body).pack(side='top', fill='both')
		return body

	def input_frame(self, master):
		input_frame = tk.Frame(master)
		self.deck_selection_frame(input_frame).pack(side='top', fill='x')
		self.named_input_frame(input_frame, 'front').pack(side="top", fill="x")
		self.named_input_frame(input_frame, 'back').pack(side="top", fill="x")
		return input_frame

	def deck_selection_frame(self, master):
		_deck_selection_frame = tk.Frame(master)
		_deck_selection_frame['bg'] = self.background_color
		_deck_selection_frame['height'] = 80
		_deck_selection_frame['padx'] = 15


		_deck_selection_frame.pack_propagate(False)
		self.named_input_label(_deck_selection_frame, "Deck").pack(side='top', fill='x')
		self.deck_selection_combo(_deck_selection_frame).pack(side='top', fill='x')
		return _deck_selection_frame

	def deck_selection_combo(self, master):
		decks = self.interface.get_deck_names()
		self.inputs['deck'] = tk.StringVar(self.master)
		self.inputs['deck'].set(decks[0])
		_deck_selection_combo = tk.OptionMenu(master, self.inputs['deck'], *decks)
		_deck_selection_combo['bg'] = self.background_color
		return _deck_selection_combo

	def named_input_frame(self, master, name):
		named_input_frame = tk.Frame(master)
		named_input_frame['height'] = 120
		named_input_frame['background'] = self.background_color
		named_input_frame['padx'] = 15
		named_input_frame.pack_propagate(False)
		self.named_input_label(named_input_frame, name).pack(side='top', fill='x')
		self.named_input(named_input_frame, name).pack(side='top', fill='x')
		return named_input_frame
		
	def named_input_label(self, master, name):
		named_input_label = tk.Label(master)
		named_input_label['text'] = f"{name}:"
		named_input_label['font'] = self.input_label_font
		named_input_label['anchor'] = 'sw'
		named_input_label['bg'] = self.background_color
		named_input_label['pady'] = 15
		return named_input_label

	def named_input(self, master, name):
		named_input_frame = tk.Frame(master)
		named_input_frame['background'] = self.background_color
		
		self.named_input_entry(named_input_frame, name).pack(side='top', fill='x')

		underscore = tk.Frame(named_input_frame)
		underscore['height'] = 1
		underscore['background'] = self.input_underscore_color
		underscore.pack_propagate(False)
		underscore.pack(side='top', fill='x')
		return named_input_frame

	def named_input_entry(self, master, name):
		_named_input = tk.Entry(master)
		_named_input['bg'] = self.background_color
		_named_input['borderwidth'] = 0
		_named_input['highlightthickness'] = 0
		_named_input['font'] = self.input_font
		_named_input['justify'] = 'center'
		self.inputs[name] = _named_input
		return _named_input

	# @overriden
	def right_header_icon(self, master):
		photo = ImageTk.PhotoImage(Image.open('icons/plus.png'))
		right_header_icon = tk.Button(master, image=photo)
		right_header_icon.image = photo
		right_header_icon['highlightbackground'] = self.header_color
		right_header_icon['highlightthickness'] = 0
		right_header_icon['command'] = self.add_flashcard
		return right_header_icon
	
	# @overriden
	def left_header_icon(self, master):
		photo = ImageTk.PhotoImage(Image.open('icons/back_arrow.png'))
		left_header_icon = tk.Button(master, image=photo)
		left_header_icon.image = photo
		left_header_icon['highlightbackground'] = self.header_color
		left_header_icon['highlightthickness'] = 0
		left_header_icon['command'] = lambda: self.master.show_main_page()
		return left_header_icon

def main():
	InitialSetup.setup()
	app = tk.Tk()
	app.title("My AnkiDroid Clone")
	main = AddFlashcard(app)
	main.pack(side="top", fill="both", expand=True)
	app.geometry('400x800')
	app.mainloop()

if __name__ == '__main__':
	main()
