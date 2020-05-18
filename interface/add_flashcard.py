import tkinter as tk
from page import Page
from PIL import ImageTk, Image
from backend.interface import UserInterface

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
		if front and back:
			self.interface.create_new_card(front, back)
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
		self.named_input_frame(input_frame, 'front').pack(side="top", fill="x")
		self.named_input_frame(input_frame, 'back').pack(side="top", fill="x")
		return input_frame

	def named_input_frame(self, master, name):
		named_input_frame = tk.Frame(master)
		named_input_frame['height'] = 120
		named_input_frame['background'] = self.background_color
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
		named_input_label['padx'] = 20
		named_input_label['pady'] = 15
		return named_input_label

	def named_input(self, master, name):
		named_input_frame = tk.Frame(master)
		named_input_frame['background'] = self.background_color
		named_input_frame['padx'] = 15

		named_input = tk.Entry(named_input_frame)
		named_input['bg'] = self.background_color
		named_input['borderwidth'] = 0
		named_input['highlightthickness'] = 0
		named_input['font'] = self.input_font
		named_input['justify'] = 'center'
		named_input.pack(side='top', fill='x')

		self.inputs[name] = named_input

		underscore = tk.Frame(named_input_frame)
		underscore['height'] = 1
		underscore['background'] = self.input_underscore_color
		underscore.pack_propagate(False)
		underscore.pack(side='top', fill='x')
		return named_input_frame

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
		left_header_icon['command'] = self.go_to_main_page
		return left_header_icon

	def go_to_main_page(self):
		self.reset_inputs(self.inputs['front'], self.inputs['back'])
		self.master.main_page.show()


