import tkinter as tk
from page import Page
from PIL import ImageTk, Image
from backend.flashcards import Flashcard

class ViewAllPage(Page):

	def __init__(self, *args, **kwargs):
		self.page_name = 'All cards'
		self.master = kwargs['master']
		Page.__init__(self, *args, **kwargs)

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
	
	# @overriden
	def right_header_icon(self, master):
		photo = ImageTk.PhotoImage(Image.open('icons/plus.png'))
		right_header_icon = tk.Button(master, image=photo)
		right_header_icon.image = photo
		right_header_icon['highlightbackground'] = self.header_color
		right_header_icon['highlightthickness'] = 0
		right_header_icon['command'] = lambda: self.master.add_flashcard_page.show()
		return right_header_icon

	# @overriden
	def body_container(self, master):
		body = tk.Frame(master)
		body['background'] = self.background_color
		self.scrolling_canvas(body).pack(side='left', fill='both', expand=True)
		self.canvas_scrollbar(body).pack(side='right', fill='y')
		self._scrolling_canvas.create_window((0,0), window=self._flashcards_frame, anchor='nw', tags='self._flashcards_frame')
		self._scrolling_canvas.configure(yscrollcommand=self._canvas_scrollbar.set)
		return body

	def scrolling_canvas(self, master):
		self._scrolling_canvas = tk.Canvas(master)
		self._scrolling_canvas['bg'] = 'red'
		self.flashcards_frame(self._scrolling_canvas)
		self._scrolling_canvas.bind("<Configure>", self.onCanvasConfigure)
		return self._scrolling_canvas

	def onCanvasConfigure(self, e):
		self._scrolling_canvas.itemconfig('self._flashcards_frame', 
											width=self._scrolling_canvas.winfo_width()
		)

	def canvas_scrollbar(self, master):
		self._canvas_scrollbar = tk.Scrollbar(master)
		self._canvas_scrollbar['orient'] = 'vertical'
		self._canvas_scrollbar['command'] = self._scrolling_canvas.yview
		return self._canvas_scrollbar

	def flashcards_frame(self, master):
		self._flashcards_frame = tk.Frame(master)
		self._flashcards_frame.bind("<Configure>", self.onFrameConfigure)

		test = []
		test.append(Flashcard('car', 'samochod', 'default', 0))
		test.append(Flashcard('firestick', 'raca', 'default', 0))
		test.append(Flashcard('balon', 'baloon', 'default', 0))
		test.append(Flashcard('kura', 'chicken', 'default', 0))
		test.append(Flashcard('kat', 'killer man', 'default', 0))
		test.append(Flashcard('dupa', 'ass', 'default', 0))
		test.append(Flashcard('car', 'samochod', 'default', 0))
		test.append(Flashcard('firestick', 'raca', 'default', 0))
		test.append(Flashcard('balon', 'baloon', 'default', 0))
		test.append(Flashcard('kura', 'chicken', 'default', 0))
		test.append(Flashcard('kat', 'killer man', 'default', 0))
		test.append(Flashcard('dupa', 'ass', 'default', 0))
		test.append(Flashcard('car', 'samochod', 'default', 0))
		test.append(Flashcard('firestick', 'raca', 'default', 0))
		test.append(Flashcard('balon', 'baloon', 'default', 0))
		test.append(Flashcard('car', 'samochod', 'default', 0))
		test.append(Flashcard('firestick', 'raca', 'default', 0))
		test.append(Flashcard('balon', 'baloon', 'default', 0))
		test.append(Flashcard('kura', 'chicken', 'default', 0))
		test.append(Flashcard('kat', 'killer man', 'default', 0))
		test.append(Flashcard('dupa', 'ass', 'default', 0))
		test.append(Flashcard('car', 'samochod', 'default', 0))
		test.append(Flashcard('firestick', 'raca', 'default', 0))
		test.append(Flashcard('balon', 'baloon', 'default', 0))
		test.append(Flashcard('kura', 'chicken', 'default', 0))
		test.append(Flashcard('kat', 'killer man', 'default', 0))
		test.append(Flashcard('dupa', 'ass', 'default', 0))
		test.append(Flashcard('car', 'samochod', 'default', 0))
		test.append(Flashcard('firestick', 'raca', 'default', 0))
		test.append(Flashcard('balon', 'baloon', 'default', 0))

		for flashcard in test:
			self.flashcard_container(self._flashcards_frame, flashcard).pack(side='top', fill='x')
			self.flashcard_divider(self._flashcards_frame).pack(side='top', fill='x')
		return self._flashcards_frame

	def onFrameConfigure(self, event):
		self._scrolling_canvas.configure(scrollregion=self._scrolling_canvas.bbox("all"))

	def flashcard_container(self, master, flashcard):
		_flashcard_container = tk.Frame(master)
		_flashcard_container['bg'] = self.background_color
		_flashcard_container['heigh'] = 50
		_flashcard_container['padx'] = 15
		_flashcard_container['pady'] = 10

		self.front_label(_flashcard_container, flashcard) \
		 	.grid(row=0, column=0, sticky='wesn')
		self.back_label(_flashcard_container, flashcard) \
			.grid(row=0, column=1, sticky='wesn')
		self.edit_button(_flashcard_container, flashcard) \
			.grid(row=0, column=2, sticky='s')
		self.remove_button(_flashcard_container, flashcard) \
			.grid(row=0, column=3, sticky='s')

		_flashcard_container.grid_columnconfigure(0, weight=10, uniform='a')
		_flashcard_container.grid_columnconfigure(1, weight=10, uniform='a')
		_flashcard_container.grid_columnconfigure(2, weight=2, uniform='a')
		_flashcard_container.grid_columnconfigure(3, weight=2, uniform='a')

		return _flashcard_container

	def front_label(self, master, flashcard):
		_front_label = tk.Label(master)
		_front_label['text'] = flashcard.front
		_front_label['anchor'] = 'sw'
		_front_label['bg'] = self.background_color
		return _front_label

	def back_label(self, master, flashcard):
		_back_label = tk.Label(master)
		_back_label['text'] = flashcard.back
		_back_label['bg'] = self.background_color
		_back_label['anchor'] = 'sw'
		return _back_label

	def remove_button(self, master, flashcard):
		_remove_button = tk.Button(master)
		_remove_button['text'] = 'x'
		_remove_button['highlightbackground'] = self.background_color
		_remove_button['width'] = 2
		return _remove_button

	def edit_button(self, master, flashcard):
		_edit_button = tk.Button(master)
		_edit_button['text'] = 'edit'
		_edit_button['highlightbackground'] = self.background_color
		return _edit_button

	def flashcard_divider(self, master):
		_flashcard_divider = tk.Frame(master)
		_flashcard_divider['height'] = 1
		_flashcard_divider['background'] = self.divider_color
		_flashcard_divider.pack_propagate(False)
		return _flashcard_divider

	# @overridden
	def footer(self, master):
		footer = tk.Frame(master)
		return footer

if __name__ == '__main__':
	app = tk.Tk()
	app.title("My AnkiDroid Clone")
	main = ViewAllPage(master=app)
	main.pack(side="top", fill="both", expand=True)
	app.geometry('400x800')
	app.mainloop()