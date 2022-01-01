import tkinter as tk

# from awesometkinter.bidirender import add_bidi_support, render_text

# from main import Mydictionary
# Mydictionary()

root = tk.Tk()

# text display incorrectly on linux without bidi support


# # uncomment below to set a rendered text to first label
# dummyvar.set(render_text(text))
canvas = tk.Canvas(root, width=500, height=500, bg='green')
text = tk.Text(root, font='any 20', width=15, height=5)
text.tag_configure("from_right_to_left", justify="right")


def from_right_to_left():
    text.tag_add("from_right_to_left", "1.0", "end")
    text_list = text.get("1.0", 'end').split()
    print(text_list)


bt = tk.Button(root, text="from right", command=from_right_to_left)
# use canvas to set widgets
show_bt = canvas.create_window(100, 50, window=bt)
show_txt = canvas.create_window(300, 200, window=text)
canvas.pack(fill='both', expand=True)
# bt.pack()
# text.pack()
# adding bidi support for widgets
# add_bidi_support(lbl)
# add_bidi_support(text)

# now there is a new set() and get() methods to set and get text on a widget


root.mainloop()
