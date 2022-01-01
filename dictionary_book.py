from tkinter import *
from tkinter import ttk
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
        # Design your frame
        self.canvas = Canvas(self, width=750, height=550, bg="white")
        self.back_ground_app = self.canvas.create_image(0, 0, image=self.canvas_frame_photo, anchor="nw")
        self.logo_app = self.canvas.create_image(450, 0, image=self.canvas_logo, anchor="nw")
        # add a treeview table
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('Treeview', background='white', forground='white', rowheight=50,
                             font=TEXT_FIELD, fieldbackground=LIGHT_BLUE_COLOR)
        self.style.configure('Treeview.Heading', background=WHITE_COLOR, forground='white', rowheight=15,
                             font=FONT_HEADING, fieldbackground='white')
        self.style.map('Treeview', background=[('selected', ORANGE_COLOR)])
        self.style.map('Treeview.Heading', background=[('selected', LIGHT_BLUE_COLOR)])
        self.tree_view = ttk.Treeview(self, columns=('from', 'to', 'original text', 'translated text'),
                                      selectmode='browse', show="headings", height=6, padding=15)
        self.tree_view.column('from', anchor=CENTER, width=150)
        self.tree_view.column('to', anchor=CENTER, width=150)
        self.tree_view.column('original text', anchor=CENTER, width=250)
        self.tree_view.column('translated text', anchor=CENTER, width=250)
        # set treeview heading
        self.tree_view.heading('from', text='From', anchor=CENTER)
        self.tree_view.heading('to', text='To', anchor=CENTER)
        self.tree_view.heading('original text', text='Original text', anchor=CENTER)
        self.tree_view.heading('translated text', text='Translated text', anchor=CENTER)
        # show treeview widget on canvas
        self.show_tree_view = self.canvas.create_window(500, 170, window=self.tree_view)
        self.load_data_to_treeview()
        self.canvas.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)
        # Methods section

    def load_data_to_treeview(self):
        if os.path.isfile('data/my_dict.json'):
            with open('data/my_dict.json', 'r') as data_file:
                data = json.load(data_file)
                for i in data:
                    original_text = data[i]['original'].split()
                    translated_text = data[i]['original'].split()
                    first_original = ' '.join(original_text[0:3])
                    first_translated = ' '.join(translated_text[0:3])
                    self.tree_view.insert(parent='', index='end', iid=i, values=(data[i]["source"], data[i]["destination"],
                                                                                 first_original, first_translated))
