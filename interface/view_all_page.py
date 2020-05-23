import tkinter as tk
from page import Page
from PIL import ImageTk, Image

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

if __name__ == '__main__':
	app = tk.Tk()
	app.title("My AnkiDroid Clone")
	main = ViewAllPage(master=app)
	main.pack(side="top", fill="both", expand=True)
	app.geometry('400x800')
	app.mainloop()