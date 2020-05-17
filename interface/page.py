import tkinter as tk
from PIL import ImageTk, Image


class Page(tk.Frame):

	page_name = 'default'
	background_color = '#f7fff7'
	header_color = '#4ecdc4'
	divider_color = "#eef0e9"

	header_font = "SFNS", 30
	
	def __init__(self, *args, **kwargs):
		tk.Frame.__init__(self, *args, **kwargs)
		self.header(self, self.page_name).pack(side='top', fill='x')
		self.body_container(self).pack(side='top', fill='both', expand='yes')
		self.footer(self).pack(side='bottom', fill='x')

	def show(self):
		self.lift()

	def header(self, master, title):
		header = tk.Frame(master)
		header['height'] = 50
		header['background'] = self.header_color
		header.pack_propagate(False)
		self.left_header_icon(header).pack(side='left', fill='y')
		self.header_title(header, title).pack(side='left', expand='yes', fill='both')
		self.right_header_icon(header).pack(side='right', fill='y')
		return header

	def left_header_icon(self, master):
		photo = ImageTk.PhotoImage(Image.open('icons/back_arrow.png'))
		left_header_icon = tk.Button(master, image=photo)
		left_header_icon.image = photo
		left_header_icon['highlightbackground'] = self.header_color
		left_header_icon['highlightthickness'] = 0
		left_header_icon['command'] = lambda: self.master.main_page.show()
		return left_header_icon

	def right_header_icon(self, master):
		photo = ImageTk.PhotoImage(Image.open('icons/chart.png'))
		right_header_icon = tk.Label(master, image=photo)
		right_header_icon.image = photo
		right_header_icon['bg'] = self.header_color
		return right_header_icon

	def header_title(self, master, text):
		header_title = tk.Label(master)
		header_title['text'] = text
		header_title['bg'] = self.header_color
		header_title['fg'] = self.background_color
		header_title['font'] = 'Nunito Sans', 20
		header_title['anchor'] = 'sw'
		header_title['padx'] = 20
		header_title['pady'] = 7
		return header_title

	def body_container(self, master):
		body = tk.Frame(master)
		body['background'] = self.background_color
		return body

	def footer(self, master):
		footer = tk.Frame(master)
		footer['height'] = 50
		footer['background'] = self.header_color
		return footer