from tkinter import *
from tkinter import ttk
import json
import os
from tkinter import messagebox
import translation_frame as tf

# All Sources from colors and Fonts
WHITE_COLOR = "#eaeaea"
LIGHT_BLUE_COLOR = "#3fc1c9"
TEXT_FORGROUND_COLOR = "#364f6b"
ORANGE_COLOR = "#fe5b24"
LIGHT_PINK = "#ffe5de"
VERY_LIGHT_PINK = "#ffe4dd"
LIGHT_GREEN = "#18a795"
FONT_HEADING = ("Varela Round", 15, "bold")
FONT_PARAGRAPH = ("Varela Round", 13, "bold")
FONT_MENU = ("Varela Round", 9, "bold")
TEXT_FIELD = ('any 20', 15, 'bold')


class DictionaryBook(Frame):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.config(bg=WHITE_COLOR, width=1000, height=800)
        # set all photos that I am going to use
        self.canvas_frame_photo = PhotoImage(file="img/canvas_bg.png")
        self.canvas_logo = PhotoImage(file="img/app_logo.png")
        self.delete_photo = PhotoImage(file="img/exit_window.png")
        self.show_details_photo = PhotoImage(file="img/book_b.png")
        self.previous_photo = PhotoImage(file="img/previous_b.png")
        self.align_right_img = PhotoImage(file="img/align_right.png")
        self.align_left_img = PhotoImage(file="img/align_left.png")
        self.align_center_img = PhotoImage(file="img/align_center.png")
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
        self.show_tree_view = self.canvas.create_window(500, 300, window=self.tree_view)
        self.load_data_to_treeview()
        # Set text field to display the original text
        # right text Fields
        self.from_text_field = Text(self, bg=LIGHT_PINK, fg=ORANGE_COLOR, font=TEXT_FIELD, width=27, height=8,
                                    relief="sunken", bd=5, pady=5,
                                    padx=5, highlightthickness=5, wrap=WORD)

        self.from_text_field.config(highlightcolor=LIGHT_PINK, highlightbackground=LIGHT_PINK)

        # left text Fields
        self.to_text_field = Text(self, bg=LIGHT_PINK, fg=ORANGE_COLOR, font=TEXT_FIELD, width=27, height=8,
                                  relief="sunken",
                                  bd=5, pady=5,
                                  padx=5, highlightthickness=5, wrap=WORD)
        self.to_text_field.config(highlightcolor=LIGHT_PINK, highlightbackground=LIGHT_PINK)
        # set show more information button
        self.more_label = Label(self, text="Show full", font=FONT_HEADING, fg=TEXT_FORGROUND_COLOR,
                                background="white")
        self.more_button = Button(self, image=self.show_details_photo, bg="white", highlightthickness=0,
                                  activebackground="white",
                                  bd=0, cursor="hand2", command=self.show_full_text)
        # set delete button
        self.delete_label = Label(self, text="Delete", font=FONT_HEADING, fg=TEXT_FORGROUND_COLOR,
                                  background="white")
        self.delete_button = Button(self, image=self.delete_photo, bg="white", highlightthickness=0,
                                    activebackground="white",
                                    bd=0, cursor="hand2", command=self.delete_data)
        # set back button
        self.previous_button = Button(self, image=self.previous_photo, bg=VERY_LIGHT_PINK, highlightthickness=0,
                                      activebackground=VERY_LIGHT_PINK,
                                      bd=0, cursor="hand2",width=50, height=60, command=self.return_home)
        # set alignment buttons
        # Left side
        self.align_left_button_l = Button(self, image=self.align_left_img, bg="white", highlightthickness=0,
                                          activebackground="white",
                                          bd=0, cursor="hand2", command=lambda: self.align_from_text('left'))
        self.align_center_button_l = Button(self, image=self.align_center_img, bg="white", highlightthickness=0,
                                            activebackground="white",
                                            bd=0, cursor="hand2", command=lambda: self.align_from_text('center'))
        self.align_right_button_l = Button(self, image=self.align_right_img, bg="white", highlightthickness=0,
                                           activebackground="white",
                                           bd=0, cursor="hand2", command=lambda: self.align_from_text('right'))

        # Right Side
        self.align_left_button_r = Button(self, image=self.align_left_img, bg="white", highlightthickness=0,
                                          activebackground="white",
                                          bd=0, cursor="hand2", command=lambda: self.align_to_text('left'))
        self.align_center_button_r = Button(self, image=self.align_center_img, bg="white", highlightthickness=0,
                                            activebackground="white",
                                            bd=0, cursor="hand2", command=lambda: self.align_to_text('center'))
        self.align_right_button_r = Button(self, image=self.align_right_img, bg="white", highlightthickness=0,
                                           activebackground="white",
                                           bd=0, cursor="hand2", command=lambda: self.align_to_text('right'))

        self.show_align_left_button_l = self.canvas.create_window(85, 730, anchor="nw", window=self.align_left_button_l)
        self.show_align_center_button_l = self.canvas.create_window(225, 730, anchor="nw",
                                                                    window=self.align_center_button_l)
        self.show_align_right_button_l = self.canvas.create_window(367, 730, anchor="nw",
                                                                   window=self.align_right_button_l)
        self.show_align_left_button_r = self.canvas.create_window(590, 730, anchor="nw",
                                                                  window=self.align_left_button_r)
        self.show_align_center_button_r = self.canvas.create_window(740, 730, anchor="nw",
                                                                    window=self.align_center_button_r)
        self.show_align_right_button_r = self.canvas.create_window(876, 730, anchor="nw",
                                                                   window=self.align_right_button_r)
        self.show_previous_button = self.canvas.create_window(0, 350, anchor='nw', window=self.previous_button)
        self.show_delete_button = self.canvas.create_window(460, 700, anchor='nw', window=self.delete_button)
        self.show_delete_label = self.canvas.create_window(455, 655, anchor='nw', window=self.delete_label)
        self.show_more_button = self.canvas.create_window(445, 540, anchor='nw', window=self.more_button)
        self.show_more_label = self.canvas.create_window(445, 500, anchor='nw', window=self.more_label)
        self.show_to_text_field = self.canvas.create_window(590, 500, anchor="nw", window=self.to_text_field)
        self.show_from_text_field = self.canvas.create_window(84, 500, anchor="nw", window=self.from_text_field)
        self.canvas.pack(fill="both", expand=True)
        self.pack(fill="both", expand=True)
        # Methods section

    def load_data_to_treeview(self):
        if os.path.isfile('data/my_dict.json'):
            with open('data/my_dict.json', 'r') as data_file:
                data = json.load(data_file)
                for i in data:
                    original_text = data[i]['original'].split()
                    translated_text = data[i]['translated'].split()
                    first_original = ' '.join(original_text[0:3])
                    first_translated = ' '.join(translated_text[0:3])
                    self.tree_view.insert(parent='', index='end', iid=i,
                                          values=(data[i]["source"], data[i]["destination"],
                                                  first_original, first_translated))

    def return_home(self):
        self.destroy()
        tf.TranslationFrame(self.root)

    def align_from_text(self, tag):
        current_tags = self.from_text_field.tag_names('1.0')
        self.from_text_field.tag_configure(tag, justify=tag)
        if len(current_tags) > 0:
            if tag not in current_tags:
                self.from_text_field.tag_add(tag, '1.0', 'end')
                for i in current_tags:
                    self.from_text_field.tag_remove(i, '1.0', 'end')
            else:
                for i in current_tags:
                    self.from_text_field.tag_remove(i, '1.0', 'end')
        else:
            self.from_text_field.tag_add(tag, '1.0', 'end')

    def align_to_text(self, tag):
        current_tags = self.to_text_field.tag_names('1.0')
        self.to_text_field.tag_configure(tag, justify=tag)
        if len(current_tags) > 0:
            if tag not in current_tags:
                self.to_text_field.tag_add(tag, '1.0', 'end')
                for i in current_tags:
                    self.to_text_field.tag_remove(i, '1.0', 'end')
            else:
                for i in current_tags:
                    self.to_text_field.tag_remove(i, '1.0', 'end')
        else:
            self.to_text_field.tag_add(tag, '1.0', 'end')

    def show_full_text(self):
        try:
            self.row_selected_id = self.tree_view.selection()[0]
        except IndexError:
            messagebox.showinfo(title="attention", message="Please select any row from the table first.")
        else:
            with open('data/my_dict.json', 'r') as data_file:
                data = json.load(data_file)
                original_text = data[self.row_selected_id]['original']
                translated_text = data[self.row_selected_id]['translated']
                self.from_text_field.delete('1.0', 'end')
                self.to_text_field.delete('1.0', 'end')
                self.from_text_field.insert('1.0', original_text)
                self.to_text_field.insert('1.0', translated_text)

    def delete_data(self):
        confirmation = messagebox.askyesno(title="Deletion confirmation", message="Are you sure you want to delete this row?")
        if confirmation:
            try:
                self.row_selected_id = self.tree_view.selection()[0]
            except IndexError:
                messagebox.showinfo(title="attention", message="Please select any row from the table first.")
            else:
                with open("data/my_dict.json", 'r') as data_file:
                    data = json.load(data_file)
                    del data[self.row_selected_id]
                    data.update(data)
                with open("data/my_dict.json", 'w') as data_file:
                    json.dump(data, data_file, indent=4)

                self.from_text_field.delete('1.0', 'end')
                self.to_text_field.delete('1.0', 'end')
                self.tree_view.delete(self.row_selected_id)







