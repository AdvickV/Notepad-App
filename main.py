from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os

class NotepadApp(Tk):
	def __init__(self):
		super().__init__()

		self.iconbitmap("logo.ico")
		self.title("Notepad")
		self.geometry("700x596")


		self.scrollbar = Scrollbar(self)
		self.scrollbar.pack(side=RIGHT, fill=Y)
		self.text_box = Text(self, height=37, width=87, wrap=WORD, yscrollcommand=self.scrollbar.set)
		self.text_box.pack()
		self.scrollbar.config(command=self.text_box.yview)

		self.main_menubar = Menu(self)
		self.rc_menubar = Menu(self, tearoff=0)
		self.rc_menubar.add_command(label="Select All", command=self.select_all)
		self.rc_menubar.add_command(label="Cut", command=self.cut)
		self.rc_menubar.add_command(label="Copy", command=self.copy)	
		self.rc_menubar.add_command(label="Paste", command=self.paste)

		self.text_box.bind("<Button-3>", self.open_rc_menu)

		# File Menu
		self.file_menu = Menu(self.main_menubar, tearoff=0)
		self.file_menu.add_command(label="New", command=self.new_file)
		self.file_menu.add_command(label="Open", command=self.open_file)
		self.file_menu.add_command(label="Save", command=self.save_file)
		self.file_menu.add_command(label="Exit", command=self.quit)
		self.main_menubar.add_cascade(label="File", menu=self.file_menu)

		# Edit Menu
		self.edit_menu = Menu(self.main_menubar, tearoff=0)
		self.edit_menu.add_command(label="Select All", command=self.select_all)
		self.edit_menu.add_command(label="Cut", command=self.cut)
		self.edit_menu.add_command(label="Copy", command=self.copy)
		self.edit_menu.add_command(label="Paste", command=self.paste)
		self.main_menubar.add_cascade(label="Edit", menu=self.edit_menu)

		# Help Menu
		self.help_menu = Menu(self.main_menubar, tearoff=0)
		self.help_menu.add_command(label="About", command=self.show_about)
		self.main_menubar.add_cascade(label="Help", menu=self.help_menu)

		self.config(menu=self.main_menubar)
		self.mainloop()

	def quit(self):
		self.destroy()

	def open_rc_menu(self, event):
		try:
			self.rc_menubar.tk_popup(event.x_root, event.y_root)
		finally:
			self.rc_menubar.grab_release()

	def open_file(self):
		self.file_path = askopenfilename(defaultextension=".txt", filetypes=[("Text Documents", "*.txt"),
																   ("All Files", "*.*")])

		if not self.file_path:
			self.file_path = None
		else:
			self.title(f"{os.path.basename(self.file_path)} - Notepad")
			self.text_box.delete("1.0", END)

			with open(self.file_path) as file:
				self.text_box.insert("1.0", file.read())

	def new_file(self):
		self.title("Untitled - Notepad")
		self.text_box.delete("1.0", END)
		self.file_path = None

	def save_file(self):
		try:
			if self.file_path:
				pass
		except AttributeError:
			self.file_path = None

		if not self.file_path:
			 self.file_path = asksaveasfilename(initialfile="Untitled.txt",
												defaultextension=".txt",
												filetypes=[("Text Documents", "*.txt"),
															("All Files", "*.*")])
			 if not self.file_path:
			 	self.file_path = None 
			 else:
			 	with open(self.file_path, "w") as file:
			 		file.write(self.text_box.get("1.0", END))

			 	self.title(f"{os.path.basename(self.file_path)} - Notepad")
		else:
			with open(self.file_path, "w") as file:
				file.write(self.text_box.get("1.0", END))


	def show_about(self):
		showinfo("About", "This program is created by AdvickV.")

	def select_all(self):
		self.text_box.tag_add(SEL, "1.0", END)

	def cut(self):
		self.text_box.event_generate("<<Cut>>")

	def copy(self):
		self.text_box.event_generate("<<Copy>>")

	def paste(self):
		self.text_box.event_generate("<<Paste>>")

app = NotepadApp()