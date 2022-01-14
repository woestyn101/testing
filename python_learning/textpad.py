from cgitb import text
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
import os, sys
import win32print
import win32api


root = Tk()
root.title("Marius's editor")
root.iconbitmap("pad_logo.ico")
root.geometry("1200x720")

# set var for open file name
global open_status_name
open_status_name = False

global selected
selected = False

# create new file function
def new_file():
    my_text.delete("1.0", END)
    root.title("New File")
    status_bar.config(text="New File       ")

    global open_status_name
    open_status_name = False


# select all function
def select_all(e):
    # add sel tag
    my_text.tag_add("sel", "1.0", "end")


# clear all function
def clear_all():
    my_text.delete(1.0, END)


# print file funcion
def print_file():
    # printer_name = win32print.GetDefaultPrinter()
    # status_bar.config(text=printer_name)
    # grab file name
    file_to_print = filedialog.askopenfilename(
        initialdir="d:/python_01/txt_editor",
        title="Open File",
        filetypes=(
            ("Text Files", "*.txt"),
            ("HTML Files", "*.html"),
            ("Python Files", "*.py"),
            ("All Files", "*.*"),
        ),
    )
    if file_to_print:
        win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)


# Open file function


def open_file():
    my_text.delete("1.0", END)
    # grab file name
    text_file = filedialog.askopenfilename(
        initialdir="d:/python_01/txt_editor",
        title="Open File",
        filetypes=(
            ("Text Files", "*.txt"),
            ("HTML Files", "*.html"),
            ("Python Files", "*.py"),
            ("All Files", "*.*"),
        ),
    )
    # check to see if there is a filename
    if text_file:
        global open_status_name
        open_status_name = text_file

    # update status bars
    name = text_file
    status_bar.config(text=f"{name}     ")
    name = name.replace("D:/python_01/txt_editor/", "")
    root.title(f"{name}")

    # open the file
    text_file = open(text_file, "r")
    content = text_file.read()
    # add file to textbox
    my_text.insert(END, content)


# change all text color


def all_text_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(fg=my_color)


# change selected text color
def text_color():

    # pick a color
    my_color = colorchooser.askcolor()[1]
    if my_color:
        # status_bar.config(text=my_color)

        color_font = font.Font(my_text, my_text.cget("font"))

        # configure a tag
        my_text.tag_configure("colored", font=color_font, foreground=my_color)

        # define current tags
        current_tags = my_text.tag_names("sel.first")

        # if statement to check if tag has been set

        if "colored" in current_tags:
            my_text.tag_remove("colored", "sel.first", "sel.last")
        else:
            my_text.tag_add("colored", "sel.first", "sel.last")


def italics_it():
    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.configure(slant="italic")

    # configure a tag
    my_text.tag_config("italic", font=italics_font)

    # define current tags
    current_tags = my_text.tag_names("sel.first")

    # if statement to check if tag has been set

    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")


def save_as_file():
    text_file = filedialog.asksaveasfilename(
        defaultextension=".*",
        initialdir="d:/python_01/txt_editor",
        title="Save file",
        filetypes=(
            ("Text Files", "*.txt"),
            ("HTML Files", "*.html"),
            ("Python Files", "*.py"),
            ("All  Files", "*.*"),
        ),
    )
    if text_file:
        name = text_file
        status_bar.config(text=f"Saved: {name}     ")
        name = name.replace("D:/python_01/txt_editor/", "")
        root.title(f"{name}")

    # save the file
    text_file = open(text_file, "w")
    text_file.write(my_text.get(1.0, END))
    text_file.close()


# save file function
def save_file():
    global open_status_name
    if open_status_name:
        # save the file
        text_file = open(open_status_name, "w")
        text_file.write(my_text.get(1.0, END))
        text_file.close()

        status_bar.config(text=f"Saved: {open_status_name}     ")
    else:
        save_as_file()


# cut text
def cut_text(e):
    global selected
    # check to see if keyboard shortcut used
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            selected = my_text.selection_get()
            my_text.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)


# copy text
def copy_text(e):
    global selected
    # check to see if we used keyboad shortcuts
    if e:
        selected = root.clipboard_get()

    if my_text.selection_get():
        selected = my_text.selection_get()
        root.clipboard_clear()
        root.clipboard_append(selected)


# paste text
def paste_text(e):
    global selected
    # check to see if keyboard shortcut used
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)


# bold it function
def bold_it():
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")

    # configure a tag
    my_text.tag_config("bold", font=bold_font)

    # define current tags
    current_tags = my_text.tag_names("sel.first")

    # if statement to check if tag has been set

    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")


def italics_it():
    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.configure(slant="italic")

    # configure a tag
    my_text.tag_config("italic", font=italics_font)

    # define current tags
    current_tags = my_text.tag_names("sel.first")

    # if statement to check if tag has been set

    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")


def bg_color():
    my_color = colorchooser.askcolor()[1]
    if my_color:
        my_text.config(bg=my_color)


# create a toolbar frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

# create main frame

my_frame = Frame(root)
my_frame.pack(pady=5)

# create Scrollbar for textbox
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# create horizontal scrollbar
hor_scroll = Scrollbar(my_frame, orient="horizontal")
hor_scroll.pack(side=BOTTOM, fill=X)


# create text box
my_text = Text(
    my_frame,
    width=97,
    height=25,
    font=("Helvetica", 16),
    selectbackground="yellow",
    selectforeground="black",
    undo=True,
    yscrollcommand=text_scroll.set,
    wrap="none",
    xscrollcommand=hor_scroll.set,
)
my_text.pack(pady=5)

# configure scroll bar
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)

# create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# add file menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save as", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Print File", command=print_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# add edit menu

edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(
    label="Cut", command=lambda: cut_text(False), accelerator="(Ctrl+x)"
)
edit_menu.add_command(
    label="Copy", command=lambda: copy_text(False), accelerator="(Ctrl+c)"
)
edit_menu.add_command(
    label="Paste", command=lambda: paste_text(False), accelerator="(Ctrl+v)"
)
file_menu.add_separator()
edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="(Ctrl+z)")
edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="(Ctrl+y)")
file_menu.add_separator()
edit_menu.add_command(
    label="Select All", command=lambda: select_all(True), accelerator="(Ctrl+a)"
)
edit_menu.add_command(label="Clear", command=clear_all, accelerator="(Ctrl+y)")


# add color  menu
color_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Colors", menu=color_menu)
color_menu.add_command(label="Selection", command=text_color)
color_menu.add_command(label="All text", command=all_text_color)
color_menu.add_command(label="Background", command=bg_color)

# add status bar to bottom
status_bar = Label(root, text="Ready    ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=15)

# edit bindings
root.bind("<Control-Key-x>", cut_text)
root.bind("<Control-Key-c>", copy_text)
root.bind("<Control-Key-v>", paste_text)
root.bind("<Control-A>", select_all)
root.bind("<Control-a>", select_all)

# create buttons for toolbar
bold_button = Button(toolbar_frame, text="Bold", command=bold_it)
bold_button.grid(row=0, column=0, sticky=W, padx=5)

italics_button = Button(toolbar_frame, text="Italics", command=italics_it)
italics_button.grid(row=0, column=1, padx=5)

undo_button = Button(toolbar_frame, text="Undo", command=my_text.edit_undo)
undo_button.grid(row=0, column=2, padx=5)

redo_button = Button(toolbar_frame, text="Redo", command=my_text.edit_redo)
redo_button.grid(row=0, column=3, padx=5)

# create text color button
text_button = Button(toolbar_frame, text="Text Color", command=text_color)
text_button.grid(row=0, column=4, padx=5)


root.mainloop()
