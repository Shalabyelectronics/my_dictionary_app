from translation_frame import *

root = Tk()
root.minsize(width=1000, height=800)
root.resizable(False, False)
root.geometry("+500+100")
root.title("My dictionary App 1.0V")
root.iconbitmap("img/my.ico")
TranslationFrame(root)
root.mainloop()
