# Simple GUI for Rot13 Encoding in Python

from tkinter import *
from tkinter import ttk

def rot13(text):
    # write your rot13 code here.
    pass

def encode(*args):
    plaintext = input_text.get()
    output_text.set(rot13(plaintext))

app = Tk()
app.title("Rot13 Encoder")

window = ttk.Frame(app, padding="5 5 10 10")
window.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

input_text = StringVar()
output_text = StringVar()

text_entry = ttk.Entry(window, width=50, textvariable=input_text)
text_entry.grid(column=2, row=1, sticky=(W, E))

text_label = ttk.Label(window, text="Enter your text here:")
text_label.grid(column=1, row=1, sticky=(W, E))

output_label = ttk.Label(window, text="Rot13 encoded text:")
output_label.grid(column=1, row=2, sticky=(W, E))

output_value = ttk.Label(window, textvariable=output_text)
output_value.grid(column=2, row=2, sticky=(W, E))

text_entry.focus()
app.bind('<Return>', encode)

app.mainloop()
