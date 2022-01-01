import json
import os
from googletrans import Translator
from tkinter import *
from tkinter import PhotoImage
import dictionary_book as dict_book

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
# ------------------------------------------------------------
# Load iso_lang json file
with open("data/iso_langs.json", "r") as iso_lang_file:
    data = json.load(iso_lang_file)
    languages_names_with_iso = {value['name']: key for key, value in data.items()}
    languages_names = [data[i]['name'] for i in data]


class TranslationFrame(Frame):
    def __init__(self, root):
        super().__init__()
        # My self window set up
        self.root = root
        self.t = None
        self.trans = None
        self.to_dest = None
        self.from_src = None
        self.from_text = None
        self.config(bg=WHITE_COLOR)
        # -------------------------------------------------------------
        # Set all the photos that I'm going to use
        self.canvas_frame_photo = PhotoImage(file="img/canvas_bg.png")
        self.canvas_logo = PhotoImage(file="img/app_logo.png")
        self.delete_photo = PhotoImage(file="img/delete_entry.png")
        self.exit_photo = PhotoImage(file="img/exit_window.png")
        self.from_photo = PhotoImage(file="img/from_lan.png")
        self.to_photo = PhotoImage(file="img/to_lan.png")
        self.translate_photo = PhotoImage(file="img/translate_button.png")
        self.save_photo = PhotoImage(file="img/my_favorite.png")
        self.show_dictionary_img = PhotoImage(file="img/show_dictionary.png")
        self.align_right_img = PhotoImage(file="img/align_right.png")
        self.align_left_img = PhotoImage(file="img/align_left.png")
        self.align_center_img = PhotoImage(file="img/align_center.png")
        # _____________________________________________________________
        # Design your frame
        self.canvas = Canvas(self, width=750, height=550, bg="white")
        self.back_ground_app = self.canvas.create_image(0, 0, image=self.canvas_frame_photo, anchor="nw")
        self.from_image_canvas = self.canvas.create_image(200, 100, image=self.from_photo)
        self.to_image_canvas = self.canvas.create_image(800, 105, image=self.to_photo)
        self.logo_app = self.canvas.create_image(450, 0, image=self.canvas_logo, anchor="nw")
        # --------------------------------------------------------------
        # Interactive widgets (That will add functionality too
        self.from_lang_label = Label(self, text="From language", font=FONT_HEADING, fg=TEXT_FORGROUND_COLOR,
                                     background="white")
        self.to_lang_label = Label(self, text="To language", font=FONT_HEADING, fg=TEXT_FORGROUND_COLOR,
                                   background="white")
        # -------------------------------------------------------------
        # Option section here we set the option menu widgets for from language
        self.from_language_sb_var = StringVar()
        self.from_language_sb_var.set(languages_names[6])
        self.pick_from_lang_option = OptionMenu(self, self.from_language_sb_var, *languages_names,
                                                command=lambda x: print(self.from_language_sb_var.get()))
        self.pick_from_lang_option.config(font=FONT_PARAGRAPH, bg="white", width=24, fg=TEXT_FORGROUND_COLOR,
                                          activebackground=LIGHT_PINK,
                                          cursor="hand2")
        self.from_lang_menu = self.nametowidget(self.pick_from_lang_option.menuname)
        self.from_lang_menu.config(font=FONT_MENU, bg="white", fg=TEXT_FORGROUND_COLOR, activebackground=LIGHT_PINK,
                                   activeforeground=TEXT_FORGROUND_COLOR, cursor="hand2")
        # -------------------------------------------------------------------
        # Option section here we set the option menu widgets for to_language
        self.to_language_sb_var = StringVar()
        self.to_language_sb_var.set(languages_names[39])
        self.pick_to_lang_option = OptionMenu(self, self.to_language_sb_var, *languages_names,
                                              command=lambda x: print(self.to_language_sb_var.get()))
        self.pick_to_lang_option.config(font=FONT_PARAGRAPH, width=24, bg="white", fg=TEXT_FORGROUND_COLOR,
                                        activebackground=LIGHT_PINK,
                                        cursor="hand2", activeforeground=TEXT_FORGROUND_COLOR)
        self.to_lang_menu = self.nametowidget(self.pick_to_lang_option.menuname)
        self.to_lang_menu.config(font=FONT_MENU, bg="white", fg=TEXT_FORGROUND_COLOR, activebackground=LIGHT_PINK,
                                 activeforeground=TEXT_FORGROUND_COLOR)
        # -------------------------------------------------------------------
        # right text Fields
        self.from_text_field = Text(self, bg=LIGHT_PINK, fg=ORANGE_COLOR, font=TEXT_FIELD, width=27, height=13,
                                    relief="sunken", bd=5, pady=5,
                                    padx=5, highlightthickness=5, wrap=WORD)

        self.from_text_field.config(highlightcolor=LIGHT_PINK, highlightbackground=LIGHT_PINK)

        # left text Fields
        self.to_text_field = Text(self, bg=LIGHT_PINK, fg=ORANGE_COLOR, font=TEXT_FIELD, width=27, height=13,
                                  relief="sunken",
                                  bd=5, pady=5,
                                  padx=5, highlightthickness=5, wrap=WORD)
        self.to_text_field.config(highlightcolor=LIGHT_PINK, highlightbackground=LIGHT_PINK)

        # -----------------------------------------------------------------
        # Set text to center to left and to right by adding three button text_left , text_center and text_right
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

        # ------------------------------------------------------------------
        # Translate label will change when click the translate button to translating
        self.translate_label = Label(self, text="Translate", font=FONT_HEADING, fg=TEXT_FORGROUND_COLOR,
                                     background="white")
        self.save_label = Label(self, text="Save", font=FONT_HEADING, fg=TEXT_FORGROUND_COLOR, background="white")
        self.empty_fields_label = Label(self, text="Empty", font=FONT_HEADING, fg=TEXT_FORGROUND_COLOR,
                                        background="white")
        self.my_dictionary_label = Label(self, text="My dictionary", font=FONT_HEADING, fg=TEXT_FORGROUND_COLOR,
                                         background="white")
        self.translate_button = Button(self, image=self.translate_photo, bg="white", highlightthickness=0,
                                       activebackground="white",
                                       bd=0, cursor="hand2", command=self.translation)

        # --------------------------------------------------------------
        # footer includes 3 icons save icon , show all save, empty field
        save_translation_button_f = Button(self, image=self.save_photo, bg="white", highlightthickness=0,
                                           activebackground="white",
                                           bd=0, cursor="hand2", command=self.save)
        show_all_saved_button_f = Button(self, image=self.show_dictionary_img, bg="white", highlightthickness=0,
                                         activebackground="white",
                                         bd=0, cursor="hand2", command=self.show_my_dictionary_treeview)
        empty_text_field_button_f = Button(self, image=self.delete_photo, bg="white", highlightthickness=0,
                                           activebackground="white",
                                           bd=0, cursor="hand2", command=self.delete_text_fields)

        # Set my widgets
        # left side
        self.show_from_lang_label = self.canvas.create_window(120, 170, anchor="nw", window=self.from_lang_label)
        self.show_from_text_field = self.canvas.create_window(40, 210, anchor="nw", window=self.from_text_field)
        self.show_align_left_button_l = self.canvas.create_window(40, 570, anchor="nw", window=self.align_left_button_l)
        self.show_align_center_button_l = self.canvas.create_window(180, 570, anchor="nw",
                                                                    window=self.align_center_button_l)
        self.show_align_right_button_l = self.canvas.create_window(330, 570, anchor="nw",
                                                                   window=self.align_right_button_l)
        self.show_pick_from_lang_o = self.canvas.create_window(40, 620, anchor="nw", window=self.pick_from_lang_option)
        # right side
        self.show_to_lang_label = self.canvas.create_window(750, 170, anchor="nw", window=self.to_lang_label)
        self.show_to_text_field = self.canvas.create_window(640, 210, anchor="nw", window=self.to_text_field)
        self.show_align_left_button_r = self.canvas.create_window(640, 570, anchor="nw",
                                                                  window=self.align_left_button_r)
        self.show_align_center_button_r = self.canvas.create_window(790, 570, anchor="nw",
                                                                    window=self.align_center_button_r)
        self.show_align_right_button_r = self.canvas.create_window(930, 570, anchor="nw",
                                                                   window=self.align_right_button_r)
        self.show_pick_to_lang_o = self.canvas.create_window(640, 620, anchor="nw", window=self.pick_to_lang_option)
        self.show_translate_label = self.canvas.create_window(425, 110, anchor="nw", height=150, width=150,
                                                              window=self.translate_label)
        self.show_save_label = self.canvas.create_window(470, 310, anchor="nw", window=self.save_label)
        self.show_empty_fields_label = self.canvas.create_window(465, 450, anchor="nw", window=self.empty_fields_label)
        self.show_my_dictionary_label = self.canvas.create_window(430, 615, anchor="nw",
                                                                  window=self.my_dictionary_label)
        # between text fields buttons
        self.show_translate_button = self.canvas.create_window(425, 195, anchor="nw", height=110, width=150,
                                                               window=self.translate_button)
        self.show_save_translation_b = self.canvas.create_window(445, 340, anchor="nw", height=110, width=110,
                                                                 window=save_translation_button_f)
        self.show_all_saved_b = self.canvas.create_window(450, 650, anchor="nw", height=110, width=110,
                                                          window=show_all_saved_button_f)
        self.show_empty_text_field_b = self.canvas.create_window(445, 490, anchor="nw", height=110, width=110,
                                                                 window=empty_text_field_button_f)
        self.canvas.pack(fill="both", expand=True)
        self.pack(fill='both', expand=True)

    # Methods section
    def translation(self):
        self.to_text_field.delete('1.0', 'end')
        self.from_text = self.from_text_field.get("1.0", "end")
        self.from_src = languages_names_with_iso[self.from_language_sb_var.get()]
        self.to_dest = languages_names_with_iso[self.to_language_sb_var.get()]
        self.trans = Translator()
        try:
            self.t = self.trans.translate(self.from_text, src=self.from_src, dest=self.to_dest)
        except ValueError:
            pass
            # add a message box that this language are not supported yet
        else:
            self.to_text_field.insert("1.0", self.t.text)

    def save(self):
        try:
            if len(self.from_language_sb_var.get()) > 0 and len(
                    self.to_language_sb_var.get()) > 0 and self.t.origin is not None and self.t.text is not None:
                if os.path.isfile("data/my_dict.json"):
                    with open('data/my_dict.json', 'r') as my_dictionary_file:
                        data_file = json.load(my_dictionary_file)
                        id_list = []
                        new_id = 0
                        for i in data_file:
                            id_list.append(int(i))
                        for i in range(len(id_list)):
                            if i in id_list:
                                new_id += 1
                        data_file.update(self.data_dumps(new_id))

                    with open('data/my_dict.json', 'w') as my_dictionary_file:
                        json.dump(data_file, my_dictionary_file, indent=4)
                else:
                    with open('data/my_dict.json', 'w') as my_dictionary_file:
                        json.dump(self.data_dumps(0), my_dictionary_file, indent=4)
        except AttributeError:
            # Add a message box her
            print("is not ready")
            pass
        else:
            print("everything is ready")

    def delete_text_fields(self):
        self.from_text_field.delete('1.0', 'end')
        self.to_text_field.delete('1.0', 'end')

    def data_dumps(self, new_id):
        new_data = {
            new_id: {
                "source": self.from_language_sb_var.get(),
                "destination": self.to_language_sb_var.get(),
                "original": self.t.origin,
                "translated": self.t.text

            }
        }
        return new_data

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

    def show_my_dictionary_treeview(self):
        self.destroy()
        dict_book.DictionaryBook(self.root)


#
# trans = Translator()
# with open("iso_langs.json", "r") as iso_langs_file:
#     data = json.load(iso_langs_file)
#
# # check_lan = trans.detect("بنات")
# # print(check_lan)
# t = trans.translate("أنا اسمي ماجد", dest="en", src="ar")
# print(
#     f"We are translate it from {data[t.src]['name']} to {data[t.dest]['name']} and the orginal word is {t.origin} > {t.text}")

'''
To fix 
googletrans AttributeError: 'NoneType' object has no attribute 'group'

just install the update
pip install googletrans==3.1.0a0
'''
