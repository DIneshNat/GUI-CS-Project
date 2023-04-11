from tkinter import ttk
import tkinter as tk
window = tk.Tk()

def farCels(farDe):
    farDe = farDe -32
    celDe = farDe/1.8
    return celDe

def celsFar(celDe):
    celDe = celDe * 1.8
    farDe = celDe + 32
    return farDe

def milKM(mil):
    km = mil * 1.609
    return km

def kmMil(km):
    mil = km/1.609
    return mil

title = tk.Label(text="Unit Converter", font=("Arial Bold", 40), width = 15, height = 2, fg = "white", bg = "#34A2FE",)
title.pack()

unitLabel = tk.Label(text="Choose Units")
unitLabel.pack()

blankLabel = tk.Label(text="")
blankLabel.pack()

combo = ttk.Combobox()
combo = ttk.Combobox(
    state="readonly",
    values=["Fahrenheit to Celsius", "Celsius to Fahrenheit", "Miles to Km", "Km to Miles"]
)
combo.place(x=70, y=120)

numberLabel = tk.Label(text="Enter Number")
insertBox = tk.Entry()
numberLabel.place(x=120, y=150)
insertBox.place(x=70, y=170)

enterButton = tk.Button(
    text ="Convert",
    width = 5,
    height = 2,
    bg = "grey",
    fg= "#34A2FE",
    relief = tk.RAISED,
)
res = 0
lens = 0
xDim = 155
def handle_click(event):
    numberLabel = tk.Label(text="", height = 100, width = 100)
    numberLabel.place(x=0, y=290)
    print("The button was clicked!")
    selection = combo.get()
    answer = insertBox.get()
    answer = int(answer)
    if selection == "Fahrenheit to Celsius":
        res = farCels(answer)
    if selection == "Celsius to Fahrenheit":
        res = celsFar(answer)
    if selection == "Miles to Km":
        res = milKM(answer)
    if selection == "Km to Miles":
        res = kmMil(answer)
    res = str(res)
    print(res)
    result = tk.Label(text = res)
    lens = len(res)
    print(lens)
    xDim = 145-lens
    print(xDim)
    result.place(x=xDim, y=290)
enterButton.bind("<Button-1>", handle_click)

enterButton.place(x=120, y=210)

resultLabel = tk.Label(text="Result:")
result = tk.Label()
resultLabel.place(x=140, y=270)
result.place(x=xDim, y=290)

window.mainloop()

