from tkinter import *
import json
import os
from tkinter import messagebox

# All Sources from colors and Fonts
WHITE_COLOR = "#eaeaea"
LIGHT_BLUE_COLOR = "#3fc1c9"
TEXT_FORGROUND_COLOR = "#364f6b"
ORANGE_COLOR = "#fe5b24"
LIGHT_PINK = "#ffe5de"
LIGHT_GREEN = "#18a795"
FONT_HEADING = ("Varela Round", 15, "bold")
FONT_PARAGRAPH = ("Varela Round", 13, "bold")
FONT_MENU = ("Varela Round", 9, "bold")
TEXT_FIELD = ('any 20', 15, 'bold')


class DictionaryBook(Frame):
    def __init__(self, root):
        super().__init__()
        self.config(bg=WHITE_COLOR, width=1000, height=800)
        # set all photos that I am going to use
        self.canvas_frame_photo = PhotoImage(file="img/canvas_bg.png")
        self.canvas_logo = PhotoImage(file="img/app_logo.png")
        self.delete_photo = PhotoImage(file="img/exit_window.png")
        self.show_details_photo = PhotoImage(file="img/book_b.png")
        self.previous_photo = PhotoImage(file="img/previous_b.png")

        self.pack(fill="both", expand=True)





