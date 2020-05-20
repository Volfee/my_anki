import tkinter as tk
from main_page import MainPage
from add_flashcard import AddFlashcard
from review_page import ReviewPage

class MainView(tk.Frame):
	def __init__(self, *args, **kwargs):
		tk.Frame.__init__(self, *args, **kwargs)
		self.add_flashcard_page = AddFlashcard(master=self)
		self.main_page = MainPage(master=self)
		
		self.container = tk.Frame(self)
		self.container.pack(side="top", fill="both", expand=True)
		self.main_page.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
		self.add_flashcard_page.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
		

		self.main_page.show()

	def create_new_review_page(self, review):
		self.review_page = ReviewPage(master=self, review=review)
		self.review_page.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)

app = tk.Tk()
app.title("My AnkiDroid Clone")
main = MainView(app)
main.pack(side="top", fill="both", expand=True)
app.geometry('400x800')
app.mainloop()